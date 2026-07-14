import pandas as pd
from src.kpi_calculator import calculate_kpis

def test_total_sales():
    df = pd.DataFrame({
        "sales": [100, 200],
        "profit": [20, 40],
        "order_id": ["A", "B"],
        "customer_id": ["C1", "C2"],
        "quantity": [1, 2],
        "region": ["West", "West"],
        "category": ["A", "A"],
        "product_name": ["P1", "P2"],
        "sales_person": ["S1", "S1"]
    })
    result = calculate_kpis(df)
    assert result.loc[0, "total_sales"] == 300
