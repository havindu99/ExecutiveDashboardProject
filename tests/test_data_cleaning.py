import pandas as pd
from src.data_cleaning import clean_data

def test_duplicate_orders_are_removed():
    df = pd.DataFrame({
        "order_id": ["A", "A"],
        "order_date": ["2026-01-01", "2026-01-01"],
        "quantity": [1, 1],
        "unit_price": [100, 100],
        "discount": [0, 0],
        "sales": [100, 100],
        "profit": [20, 20],
        "category": ["Test", "Test"]
    })
    cleaned = clean_data(df)
    assert len(cleaned) == 1
