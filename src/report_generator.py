from datetime import datetime
from pathlib import Path
import pandas as pd
from src.config import REPORT_DIR
from src.logger import get_logger

logger = get_logger(__name__)

def generate_text_report(kpi_df: pd.DataFrame, output_path: Path | None = None) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    if output_path is None:
        output_path = REPORT_DIR / "executive_summary.txt"

    row = kpi_df.iloc[0]

    report = f"""
EXECUTIVE DASHBOARD SUMMARY
Generated: {datetime.now():%Y-%m-%d %H:%M}

FINANCIAL PERFORMANCE
Total Sales: LKR {row['total_sales']:,.2f}
Total Profit: LKR {row['total_profit']:,.2f}
Profit Margin: {row['profit_margin_percent']:.2f}%
Average Order Value: LKR {row['average_order_value']:,.2f}

BUSINESS ACTIVITY
Total Orders: {int(row['total_orders']):,}
Total Customers: {int(row['total_customers']):,}
Units Sold: {int(row['units_sold']):,}

TOP PERFORMERS
Top Region: {row['top_region']}
Top Category: {row['top_category']}
Top Product: {row['top_product']}
Top Sales Person: {row['top_sales_person']}
""".strip()

    output_path.write_text(report, encoding="utf-8")
    logger.info("Executive report generated at %s", output_path)
    return output_path
