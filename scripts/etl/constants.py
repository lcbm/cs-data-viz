""" File with the definitions of constants for the ETL scripts. """
SCRIPTS_DIR = "scripts"
SCRIPTS_ETL_DIR = f"{SCRIPTS_DIR}/etl"
SCRIPTS_ETL_TRANSFORM = f"{SCRIPTS_ETL_DIR}/transform.sh"

VENV_BIN = ".venv/bin"
VENV_KAGGLE_BIN = f"{VENV_BIN}/kaggle"

DOCKER_DIR = "docker"
ENVARS_DIR = f"{DOCKER_DIR}/env.d"
DATA_DIR = f"{DOCKER_DIR}/database/data"
DATA_FILE_EXTENSION = ".csv"

OLIST_TABLE_CATEGORY_TRANSLATIONS = "product_category_name_translation"
OLIST_TABLE_GEOLOCATION = "olist_geolocation_dataset"
OLIST_TABLE_CUSTOMERS = "olist_customers_dataset"
OLIST_TABLE_ORDERS = "olist_orders_dataset"
OLIST_TABLE_PRODUCTS = "olist_products_dataset"
OLIST_TABLE_SELLERS = "olist_sellers_dataset"
OLIST_TABLE_ORDER_PAYMENTS = "olist_order_payments_dataset"
OLIST_TABLE_ORDER_REVIEWS = "olist_order_reviews_dataset"
OLIST_TABLE_ORDER_ITEMS = "olist_order_items_dataset"

OLIST_DATASET_TABLES = [
    OLIST_TABLE_CATEGORY_TRANSLATIONS,
    OLIST_TABLE_GEOLOCATION,
    OLIST_TABLE_CUSTOMERS,
    OLIST_TABLE_ORDERS,
    OLIST_TABLE_PRODUCTS,
    OLIST_TABLE_SELLERS,
    OLIST_TABLE_ORDER_PAYMENTS,
    OLIST_TABLE_ORDER_REVIEWS,
    OLIST_TABLE_ORDER_ITEMS,
]

OLIST_TABLE_CATEGORY_TRANSLATIONS_TYPE_MAP = {
    "product_category_name": str,
    "product_category_name_english": str,
}
OLIST_TABLE_CATEGORY_TRANSLATIONS_COLUMNS = (
    OLIST_TABLE_CATEGORY_TRANSLATIONS_TYPE_MAP.keys()
)

OLIST_TABLE_GEOLOCATION_TYPE_MAP = {
    "geolocation_zip_code_prefix": str,
    "geolocation_lat": float,
    "geolocation_lng": float,
    "geolocation_city": str,
    "geolocation_state": str,
}
OLIST_TABLE_GEOLOCATION_COLUMNS = OLIST_TABLE_GEOLOCATION_TYPE_MAP.keys()

OLIST_TABLE_CUSTOMERS_TYPE_MAP = {
    "customer_id": str,
    "customer_unique_id": str,
    "customer_zip_code_prefix": str,
    "customer_city": str,
    "customer_state": str,
}
OLIST_TABLE_CUSTOMERS_COLUMNS = OLIST_TABLE_CUSTOMERS_TYPE_MAP.keys()

OLIST_TABLE_ORDERS_TYPE_MAP = {
    "order_id": str,
    "customer_id": str,
    "order_status": str,
    "order_purchase_date": str,
    "order_approved_at": str,
    "order_delivered_carrier_date": str,
    "order_delivered_customer_date": str,
    "order_estimated_delivery_date": str,
}
OLIST_TABLE_ORDERS_COLUMNS = OLIST_TABLE_ORDERS_TYPE_MAP.keys()

OLIST_TABLE_PRODUCTS_TYPE_MAP = {
    "product_id": str,
    "product_category_name": str,
    "product_name_lenght": str,
    "product_description_lenght": "Int64",
    "product_photos_qty": "Int64",
    "product_weight_g": "Int64",
    "product_length_cm": "Int64",
    "product_height_cm": "Int64",
    "product_width_cm": "Int64",
}
OLIST_TABLE_PRODUCTS_COLUMNS = OLIST_TABLE_PRODUCTS_TYPE_MAP.keys()

OLIST_TABLE_SELLERS_TYPE_MAP = {
    "seller_id": str,
    "seller_zip_code_prefix": str,
    "seller_city": str,
    "seller_state": str,
}
OLIST_TABLE_SELLERS_COLUMNS = OLIST_TABLE_SELLERS_TYPE_MAP.keys()

OLIST_TABLE_ORDER_PAYMENTS_TYPE_MAP = {
    "order_id": str,
    "payment_sequential": "Int64",
    "payment_type": str,
    "payment_installments": "Int64",
    "payment_value": float,
}
OLIST_TABLE_ORDER_PAYMENTS_COLUMNS = OLIST_TABLE_ORDER_PAYMENTS_TYPE_MAP.keys()

OLIST_TABLE_ORDER_REVIEWS_TYPE_MAP = {
    "review_id": str,
    "order_id": str,
    "review_score": "Int64",
    "review_comment_title": str,
    "review_comment_message": str,
    "review_creation_date": str,
    "review_answer_date": str,
}
OLIST_TABLE_ORDER_REVIEWS_COLUMNS = OLIST_TABLE_ORDER_REVIEWS_TYPE_MAP.keys()

OLIST_TABLE_ORDER_ITEMS_TYPE_MAP = {
    "order_id": str,
    "order_item_id": "Int64",
    "product_id": str,
    "seller_id": str,
    "shipping_limit_date": str,
    "price": float,
    "freight_value": float,
}
OLIST_TABLE_ORDER_ITEMS_COLUMNS = OLIST_TABLE_ORDER_ITEMS_TYPE_MAP.keys()

OLIST_DATASET_TABLES_TYPES_MAP = {
    OLIST_TABLE_CATEGORY_TRANSLATIONS: OLIST_TABLE_CATEGORY_TRANSLATIONS_TYPE_MAP,
    OLIST_TABLE_GEOLOCATION: OLIST_TABLE_GEOLOCATION_TYPE_MAP,
    OLIST_TABLE_CUSTOMERS: OLIST_TABLE_CUSTOMERS_TYPE_MAP,
    OLIST_TABLE_ORDERS: OLIST_TABLE_ORDERS_TYPE_MAP,
    OLIST_TABLE_PRODUCTS: OLIST_TABLE_PRODUCTS_TYPE_MAP,
    OLIST_TABLE_SELLERS: OLIST_TABLE_SELLERS_TYPE_MAP,
    OLIST_TABLE_ORDER_PAYMENTS: OLIST_TABLE_ORDER_PAYMENTS_TYPE_MAP,
    OLIST_TABLE_ORDER_REVIEWS: OLIST_TABLE_ORDER_REVIEWS_TYPE_MAP,
    OLIST_TABLE_ORDER_ITEMS: OLIST_TABLE_ORDER_ITEMS_TYPE_MAP,
}

OLIST_DATASET_TABLES_NULLABLE_COLUMNS = {
    OLIST_TABLE_CATEGORY_TRANSLATIONS: [],
    OLIST_TABLE_GEOLOCATION: [],
    OLIST_TABLE_CUSTOMERS: [],
    OLIST_TABLE_ORDERS: [],
    OLIST_TABLE_PRODUCTS: [],
    OLIST_TABLE_SELLERS: [],
    OLIST_TABLE_ORDER_PAYMENTS: [],
    OLIST_TABLE_ORDER_REVIEWS: ["review_comment_title", "review_comment_message"],
    OLIST_TABLE_ORDER_ITEMS: [],
}


def MACRO_GET_DATASET_DIR(table):
    return f"{DATA_DIR}/{table}{DATA_FILE_EXTENSION}"


def MACRO_GET_REQUIRED_COLUMNS(dataframe, table):
    nullable_cols = [
        col
        for col in dataframe.columns
        if col not in OLIST_DATASET_TABLES_NULLABLE_COLUMNS[table]
    ]
    return nullable_cols if len(nullable_cols) > 0 else None
