""" Main script to run ETL functions. """
import scripts.etl.extract as extract
import scripts.etl.transform as transform

if __name__ == "__main__":
    extract.load_kaggle_envars()
    extract.download_dataset_from_kaggle_as_zip()
    extract.unzip_dataset()

    transform.remove_non_ascii_from_datasets()
    transform.rename_files()
    dataframes = transform.load_datasets(drop_na=True)
    transform.remove_duplicates_from_geolocation(dataframes)
    transform.remove_missing_geolocation_primary_keys(dataframes)
    transform.remove_missing_customers_primary_keys(dataframes)
    transform.remove_missing_orders_primary_keys(dataframes)
    transform.remove_missing_sellers_primary_keys(dataframes)
    transform.remove_missing_products_primary_keys(dataframes)
    transform.replace_products_product_category_name(dataframes)
