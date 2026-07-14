import pandas as pd
from src.config import REQUIRED_COLUMNS
from src.logger import get_logger

logger = get_logger(__name__)

def validate_schema(df: pd.DataFrame) -> dict:
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    extra_columns = [col for col in df.columns if col not in REQUIRED_COLUMNS]

    result = {
        "is_valid": len(missing_columns) == 0,
        "missing_columns": missing_columns,
        "extra_columns": extra_columns,
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_values": int(df.isna().sum().sum())
    }

    if not result["is_valid"]:
        logger.error("Schema validation failed: %s", missing_columns)
    else:
        logger.info("Schema validation passed")

    return result
