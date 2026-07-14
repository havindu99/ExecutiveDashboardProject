from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "sales_data.csv"
INTERIM_DATA_PATH = BASE_DIR / "data" / "interim" / "sales_cleaned.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "executive_dashboard_dataset.csv"
KPI_SUMMARY_PATH = BASE_DIR / "data" / "processed" / "kpi_summary.csv"

LOG_DIR = BASE_DIR / "output" / "logs"
REPORT_DIR = BASE_DIR / "output" / "reports"

REQUIRED_COLUMNS = [
    "order_id", "order_date", "customer_id", "customer_name",
    "customer_segment", "region", "city", "category",
    "subcategory", "product_name", "sales_person", "quantity",
    "unit_price", "discount", "sales", "profit", "payment_method"
]
