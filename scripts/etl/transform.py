""" Python script to transform data. """
import csv
import os
import subprocess

import numpy as np
import pandas as pd

import scripts.etl.constants as const


def remove_non_ascii_from_datasets():
    cwd = subprocess.check_output("pwd").decode("utf-8").strip("\n")
    subprocess.run([const.SCRIPTS_ETL_TRANSFORM, const.DATA_DIR], cwd=cwd)


def rename_files():
    files = os.listdir(const.DATA_DIR)
    for filename in files:
        if filename.endswith(".csv"):
            os.remove(f"{const.DATA_DIR}/{filename}")

    for filename in files:
        if filename.endswith(".csv_new"):
            new_filename = filename.replace(".csv_new", ".csv")
            os.rename(
                f"{const.DATA_DIR}/{filename}", f"{const.DATA_DIR}/{new_filename}"
            )


def load_datasets(drop_na=False):
    dataframes = dict()
    for table in const.OLIST_DATASET_TABLES:
        csv_file = const.MACRO_GET_DATASET_DIR(table)
        dtype = const.OLIST_DATASET_TABLES_TYPES_MAP.get(table, None)
        df = pd.read_csv(csv_file, dtype=dtype)

        if drop_na is True:
            df.replace(r"^\s*$", np.nan, regex=True, inplace=True)

            subset = const.MACRO_GET_REQUIRED_COLUMNS(df, table)
            df.dropna(axis=0, subset=subset, inplace=True)

        __drop_duplicate_primary_keys(df)
        dataframes[table] = df

        dir = const.MACRO_GET_DATASET_DIR(table)
        __to_csv(df, dir)

    return dataframes


def remove_duplicates_from_geolocation(dataframes):
    df = dataframes.get(const.OLIST_TABLE_GEOLOCATION)

    df = __set_geolocation_primary_key_to_df(df, "geolocation")
    df.drop_duplicates(subset=["primary_key"], keep="last", inplace=True)
    df.drop("primary_key", axis=1, inplace=True)

    dir_geolocation = const.MACRO_GET_DATASET_DIR(const.OLIST_TABLE_GEOLOCATION)
    __to_csv(df, dir_geolocation)


def remove_missing_customers_primary_keys(dataframes):
    df_customers = dataframes.get(const.OLIST_TABLE_CUSTOMERS)
    df_orders = dataframes.get(const.OLIST_TABLE_ORDERS)

    cond_orders = df_orders["customer_id"].isin(df_customers["customer_id"])
    df_orders.drop(df_orders[~cond_orders].index, inplace=True)

    dir_orders = const.MACRO_GET_DATASET_DIR(const.OLIST_TABLE_ORDERS)
    __to_csv(df_orders, dir_orders)


def remove_missing_geolocation_primary_keys(dataframes):
    df_geolocation = dataframes.get(const.OLIST_TABLE_GEOLOCATION)
    df_geolocation = __set_geolocation_primary_key_to_df(df_geolocation, "geolocation")

    df_customers = dataframes.get(const.OLIST_TABLE_CUSTOMERS)
    df_customers = __set_geolocation_primary_key_to_df(df_customers, "customer")

    df_sellers = dataframes.get(const.OLIST_TABLE_SELLERS)
    df_sellers = __set_geolocation_primary_key_to_df(df_sellers, "seller")

    cond_customers = df_customers["primary_key"].isin(df_geolocation["primary_key"])
    cond_sellers = df_sellers["primary_key"].isin(df_geolocation["primary_key"])

    df_customers.drop(df_customers[~cond_customers].index, inplace=True)
    df_sellers.drop(df_sellers[~cond_sellers].index, inplace=True)

    df_customers = df_customers.drop("primary_key", axis=1)
    df_sellers = df_sellers.drop("primary_key", axis=1)

    dir_customers = const.MACRO_GET_DATASET_DIR(const.OLIST_TABLE_CUSTOMERS)
    __to_csv(df_customers, dir_customers)

    dir_sellers = const.MACRO_GET_DATASET_DIR(const.OLIST_TABLE_SELLERS)
    __to_csv(df_sellers, dir_sellers)


def remove_missing_orders_primary_keys(dataframes):
    df_orders = dataframes.get(const.OLIST_TABLE_ORDERS)
    df_order_payments = dataframes.get(const.OLIST_TABLE_ORDER_PAYMENTS)
    df_order_reviews = dataframes.get(const.OLIST_TABLE_ORDER_REVIEWS)
    df_order_items = dataframes.get(const.OLIST_TABLE_ORDER_ITEMS)

    cond_order_payments = df_order_payments["order_id"].isin(df_orders["order_id"])
    cond_order_reviews = df_order_reviews["order_id"].isin(df_orders["order_id"])
    cond_order_items = df_order_items["order_id"].isin(df_orders["order_id"])

    df_order_payments.drop(df_order_payments[~cond_order_payments].index, inplace=True)
    df_order_reviews.drop(df_order_reviews[~cond_order_reviews].index, inplace=True)
    df_order_items.drop(df_order_items[~cond_order_items].index, inplace=True)

    dir_order_payments = const.MACRO_GET_DATASET_DIR(const.OLIST_TABLE_ORDER_PAYMENTS)
    __to_csv(df_order_payments, dir_order_payments)

    dir_order_reviews = const.MACRO_GET_DATASET_DIR(const.OLIST_TABLE_ORDER_REVIEWS)
    __to_csv(df_order_reviews, dir_order_reviews)

    dir_order_items = const.MACRO_GET_DATASET_DIR(const.OLIST_TABLE_ORDER_ITEMS)
    __to_csv(df_order_items, dir_order_items)


def remove_missing_sellers_primary_keys(dataframes):
    df_sellers = dataframes.get(const.OLIST_TABLE_SELLERS)
    df_order_items = dataframes.get(const.OLIST_TABLE_ORDER_ITEMS)

    cond_order_payments = df_order_items["seller_id"].isin(df_sellers["seller_id"])

    df_order_items.drop(df_order_items[~cond_order_payments].index, inplace=True)

    dir_order_items = const.MACRO_GET_DATASET_DIR(const.OLIST_TABLE_ORDER_ITEMS)
    __to_csv(df_order_items, dir_order_items)


def remove_missing_products_primary_keys(dataframes):
    df_products = dataframes.get(const.OLIST_TABLE_PRODUCTS)
    df_order_items = dataframes.get(const.OLIST_TABLE_ORDER_ITEMS)

    cond_order_payments = df_order_items["product_id"].isin(df_products["product_id"])

    df_order_items.drop(df_order_items[~cond_order_payments].index, inplace=True)

    dir_order_items = const.MACRO_GET_DATASET_DIR(const.OLIST_TABLE_ORDER_ITEMS)
    __to_csv(df_order_items, dir_order_items)


def replace_products_product_category_name(dataframes):
    df_products = dataframes.get(const.OLIST_TABLE_PRODUCTS)

    df_products["product_category_name"] = df_products["product_category_name"].apply(
        lambda name: "eletroportateis"
        if name == "portateis_cozinha_e_preparadores_de_alimentos"
        else name
    )
    df_products["product_category_name"] = df_products["product_category_name"].apply(
        lambda name: "pcs" if name == "pc_gamer" else name
    )

    dir_products = const.MACRO_GET_DATASET_DIR(const.OLIST_TABLE_PRODUCTS)
    __to_csv(df_products, dir_products)


def __drop_duplicate_primary_keys(dataframe):
    first_col = dataframe.columns[0]
    if not first_col.endswith("_id"):
        return

    dataframe.drop_duplicates(subset=[first_col], keep="last", inplace=True)


def __to_csv(dataframe, dir):
    dataframe.to_csv(dir, sep=",", index=False, quoting=csv.QUOTE_NONNUMERIC)


def __set_geolocation_primary_key_to_df(dataframe, table):
    dataframe["primary_key"] = dataframe.apply(
        lambda row: str(row[f"{table}_zip_code_prefix"])
        + str(row[f"{table}_city"])
        + str(row[f"{table}_state"]),
        axis=1,
    )
    return dataframe
