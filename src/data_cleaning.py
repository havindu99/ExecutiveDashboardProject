import pandas as pd
from src.logger import get_logger

logger = get_logger(__name__)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    cleaned.columns = (
        cleaned.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    cleaned["order_date"] = pd.to_datetime(cleaned["order_date"], errors="coerce")

    numeric_columns = ["quantity", "unit_price", "discount", "sales", "profit"]
    for column in numeric_columns:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    cleaned = cleaned.drop_duplicates(subset=["order_id"], keep="first")

    cleaned["sales"] = cleaned["sales"].fillna(
        cleaned["quantity"] * cleaned["unit_price"] * (1 - cleaned["discount"])
    )

    category_profit_margin = (
        cleaned.groupby("category")["profit"]
        .transform("median")
    )
    cleaned["profit"] = cleaned["profit"].fillna(category_profit_margin)

    text_columns = cleaned.select_dtypes(include="object").columns
    for column in text_columns:
        cleaned[column] = cleaned[column].fillna("Unknown").str.strip()

    cleaned = cleaned.dropna(subset=["order_date", "order_id", "sales"])
    cleaned = cleaned[cleaned["sales"] >= 0]
    cleaned = cleaned[cleaned["quantity"] > 0]

    logger.info("Cleaned dataset contains %s rows", len(cleaned))
    return cleaned
