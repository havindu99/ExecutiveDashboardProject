import numpy as np
import pandas as pd
from src.logger import get_logger

logger = get_logger(__name__)

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    featured = df.copy()

    featured["year"] = featured["order_date"].dt.year
    featured["month_number"] = featured["order_date"].dt.month
    featured["month_name"] = featured["order_date"].dt.month_name()
    featured["year_month"] = featured["order_date"].dt.to_period("M").astype(str)
    featured["quarter"] = "Q" + featured["order_date"].dt.quarter.astype(str)
    featured["profit_margin"] = np.where(
        featured["sales"] != 0,
        featured["profit"] / featured["sales"],
        0
    )
    featured["discount_amount"] = (
        featured["quantity"] * featured["unit_price"] * featured["discount"]
    )
    featured["sales_band"] = pd.cut(
        featured["sales"],
        bins=[-1, 10000, 50000, 150000, float("inf")],
        labels=["Low", "Medium", "High", "Premium"]
    )

    logger.info("Feature engineering completed")
    return featured
