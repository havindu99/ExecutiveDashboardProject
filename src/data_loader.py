from pathlib import Path
import pandas as pd
from src.logger import get_logger

logger = get_logger(__name__)

def load_data(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    logger.info("Loading data from %s", file_path)
    df = pd.read_csv(file_path)
    logger.info("Loaded %s rows and %s columns", len(df), len(df.columns))
    return df
