# Automated Reporting Schedule

| Activity | Frequency | Time | Output |
|---|---:|---:|---|
| Source data refresh | Daily | 08:00 AM | Updated raw CSV |
| Python data pipeline | Daily | 08:05 AM | Cleaned and processed datasets |
| KPI summary generation | Daily | 08:10 AM | `kpi_summary.csv` |
| Executive report generation | Daily | 08:15 AM | Executive summary report |
| Power BI dataset refresh | Daily | 08:30 AM | Refreshed dashboard |

## Recommended Windows Task Scheduler Command

```bash
python -m automation.run_pipeline
```

Set the working directory to the project root.
