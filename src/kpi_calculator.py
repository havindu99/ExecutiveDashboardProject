import pandas as pd
from src.logger import get_logger

logger = get_logger(__name__)

def calculate_kpis(df: pd.DataFrame) -> pd.DataFrame:
    total_sales = float(df["sales"].sum())
    total_profit = float(df["profit"].sum())
    total_orders = int(df["order_id"].nunique())
    total_customers = int(df["customer_id"].nunique())

    summary = {
        "total_sales": round(total_sales, 2),
        "total_profit": round(total_profit, 2),
        "profit_margin_percent": round((total_profit / total_sales * 100), 2) if total_sales else 0,
        "total_orders": total_orders,
        "total_customers": total_customers,
        "average_order_value": round(total_sales / total_orders, 2) if total_orders else 0,
        "units_sold": int(df["quantity"].sum()),
        "top_region": df.groupby("region")["sales"].sum().idxmax(),
        "top_category": df.groupby("category")["sales"].sum().idxmax(),
        "top_product": df.groupby("product_name")["sales"].sum().idxmax(),
        "top_sales_person": df.groupby("sales_person")["sales"].sum().idxmax()
    }

    logger.info("KPI calculation completed")
    return pd.DataFrame([summary])

def monthly_performance(df: pd.DataFrame) -> pd.DataFrame:
    monthly = (
        df.groupby("year_month", as_index=False)
        .agg(
            sales=("sales", "sum"),
            profit=("profit", "sum"),
            orders=("order_id", "nunique")
        )
        .sort_values("year_month")
    )

    monthly["sales_growth_percent"] = (
        monthly["sales"].pct_change() * 100
    ).round(2)

    return monthly
