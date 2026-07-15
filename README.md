# Executive Sales Dashboard

## Overview

The Executive Sales Dashboard is a business intelligence project developed using Python and Microsoft Power BI. It provides executives with an interactive dashboard to monitor sales performance, profitability, customer insights, and regional performance.

## Features

- Executive KPI Dashboard
- Total Sales Analysis
- Total Profit Analysis
- Total Orders
- Total Customers
- Profit Margin Analysis
- Average Order Value
- Sales Trend by Year
- Sales by Region
- Sales by Category
- Top Products Analysis
- Interactive Year Filter
- Mobile Layout Dashboard
- Automated Data Pipeline

## Technologies Used

- Python 3
- Pandas
- NumPy
- OpenPyXL
- Power BI Desktop
- Git
- GitHub

## Project Structure

```
ExecutiveDashboardProject/
│
├── automation/
├── dashboard/
│   └── powerbi.pbix
├── data/
│   ├── raw/
│   ├── processed/
│   └── interim/
├── docs/
├── output/
│   ├── logs/
│   └── reports/
├── src/
├── tests/
├── README.md
└── requirements.txt
```

## KPIs

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Profit Margin
- Average Order Value

## Dashboard Visuals

- KPI Cards
- Sales Trend by Year
- Sales by Region
- Sales by Category
- Top Products by Sales
- Interactive Year Filter

## Data Pipeline

The pipeline performs:

1. Data Loading
2. Data Validation
3. Data Cleaning
4. Feature Engineering
5. KPI Calculation
6. Executive Report Generation

Run the pipeline using:

```bash
py -m automation.run_pipeline
```

## Output

The project automatically generates:

- Cleaned Dataset
- KPI Summary
- Executive Report
- Power BI Dashboard
- Dashboard Screenshots

## Author

**Havindu Perera**

SLIIT Undergraduate

GitHub:
https://github.com/havindu99

## License

This project was developed for educational and portfolio purposes.
