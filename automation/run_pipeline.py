from src.config import (
    RAW_DATA_PATH,
    INTERIM_DATA_PATH,
    PROCESSED_DATA_PATH,
    KPI_SUMMARY_PATH
)
from src.data_loader import load_data
from src.data_validator import validate_schema
from src.data_cleaning import clean_data
from src.feature_engineering import add_features
from src.kpi_calculator import calculate_kpis, monthly_performance
from src.report_generator import generate_text_report
from src.logger import get_logger

logger = get_logger(__name__)

def run_pipeline() -> None:
    logger.info("Starting executive dashboard data pipeline")

    raw_df = load_data(RAW_DATA_PATH)
    validation = validate_schema(raw_df)

    if not validation["is_valid"]:
        raise ValueError(
            f"Missing required columns: {validation['missing_columns']}"
        )

    cleaned_df = clean_data(raw_df)
    INTERIM_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(INTERIM_DATA_PATH, index=False)

    processed_df = add_features(cleaned_df)
    processed_df.to_csv(PROCESSED_DATA_PATH, index=False)

    kpi_df = calculate_kpis(processed_df)
    kpi_df.to_csv(KPI_SUMMARY_PATH, index=False)

    monthly_df = monthly_performance(processed_df)
    monthly_df.to_csv(
        PROCESSED_DATA_PATH.parent / "monthly_performance.csv",
        index=False
    )

    report_path = generate_text_report(kpi_df)

    logger.info("Pipeline completed successfully")
    print("\nPipeline completed successfully.")
    print(f"Processed dataset: {PROCESSED_DATA_PATH}")
    print(f"KPI summary: {KPI_SUMMARY_PATH}")
    print(f"Executive report: {report_path}")

if __name__ == "__main__":
    run_pipeline()
