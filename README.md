# Retail Demand Forecasting & Inventory Optimization Platform

An end-to-end data analytics and machine learning project built using Python, PostgreSQL, and Power BI to forecast retail demand, predict stockouts, and optimize inventory decisions.

## Project Objective

The objective of this project is to identify the key factors affecting:

- Future product demand
- Inventory shortages
- Reorder requirements
- Promotion-driven sales
- Competition impact on store sales
- Seasonal and monthly sales trends

## Tools & Technologies

- Python
- Pandas
- PostgreSQL
- Power BI
- Scikit-learn
- Random Forest
- VS Code


## Key Business Scenarios

- Monthly Sales Trend
- Promotion vs Non-Promotion Sales
- Competition Distance vs Sales
- Store Type Performance
- Products Needing Reorder
- Stockout Risk by Store
- Reorder Quantity Recommendation
- Best Sales Months

## Machine Learning Models

### Demand Forecasting Model
A Random Forest Regressor was built to forecast future sales based on:

- Store
- Promotion
- Month
- Competition Distance
- Previous Day Sales
- Previous Week Sales
- Rolling 7 Day Sales

### Stockout Prediction Model
A classification model was built to identify whether a product needs reorder based on:

- Inventory Level
- Demand Forecast
- Safety Stock
- Reorder Point

## Power BI Dashboard

The dashboard contains:

- KPI Cards
  - Total Sales
  - Average Sales
  - Total Stores
  - Products Needing Reorder

- Visuals
  - Monthly Sales Trend
  - Competition Distance vs Sales
  - Monthly Sales by Promotion
  - Top Products Needing Reorder
  - Sales Share by Store Type

## SQL Business Queries

Example business questions answered:

- Which stores generate the highest sales?
- Which products need urgent reorder?
- Which months have the highest sales?
- How does promotion affect sales?
- Which stores have the highest stockout risk?

## Sample Dataset Information

The original processed dataset (`final_featured_data.csv`) was larger than GitHub's file size limit (100 MB). To make the project easy to share and review, a smaller sample dataset was created.

- Original dataset size: ~142 MB
- Sample dataset size: 20,000 rows
- Sample file used in repository:
  - `data/processed/final_featured_data_sample.csv`

The sample dataset preserves the same structure and features as the original dataset, allowing recruiters and reviewers to understand the project workflow without downloading very large files.


## Results & Insights

- Promotions increased average store sales.
- Stores with closer competitors generally had lower sales.
- Certain months showed consistently higher sales demand.
- Reorder recommendations identified products likely to go out of stock.
- The demand forecasting model successfully predicted future sales trends.
- The stockout model helped identify risky inventory situations.

## How to Run

1. Clone the repository
2. Install required libraries

```bash
pip install -r requirements.txt

Run Python scripts in this order:

python/data_cleaning.py
python/merge_data.py
python/feature_engineering.py
python/demand_forecasting.py
python/stockout_prediction.py
python/reorder_recommendation.py

4. Run SQL queries from the `sql/` folder in PostgreSQL:
   - `business_queries.sql`
   - `inventory_kpis.sql`
   - `forecasting_queries.sql`

5. Open the Power BI dashboard file:

```text
powerbi_dashboard/Retail_Inventory_Dashboard.pbix


## Data Engineering Enhancements

This project was extended with data engineering concepts to simulate a real-world ETL pipeline.

Implemented features:
- Staging tables in PostgreSQL
- Fact and Dimension warehouse tables
- Incremental loading
- Schema validation
- Data quality checks
- Logging
- Automated ETL runner
- Warehouse export generation

Pipeline Flow:

```text
Raw CSV → Schema Validation → Data Quality Checks → Staging Tables → Fact/Dimension Tables → Incremental Load → Warehouse Export

##Folder structure

Retail_Inventory_Analytics/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── processed/
│   ├── staging/
│   └── warehouse/
│
├── python/
│   ├── data_cleaning.py
│   ├── merge_data.py
│   ├── feature_engineering.py
│   ├── demand_forecasting.py
│   ├── stockout_prediction.py
│   ├── reorder_recommendation.py
│   ├── load_staging_tables.py
│   ├── data_quality_checks.py
│   ├── schema_validation.py
│   ├── export_warehouse_data.py
│   └── create_sample_data.py
│
├── pipelines/
│   ├── extract_data.py
│   ├── transform_data.py
│   ├── load_data.py
│   ├── run_pipeline.py
│   └── run_etl_pipeline.py
│
├── sql/
│   ├── business_queries.sql
│   ├── forecasting_queries.sql
│   ├── inventory_kpis.sql
│   ├── insert_data.sql
│   ├── schema.sql
│   ├── staging/
│   │   └── create_staging_tables.sql
│   └── warehouse/
│       ├── create_warehouse_tables.sql
│       ├── load_fact_dimension_tables.sql
│       └── incremental_load.sql
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_forecasting_model.ipynb
│   └── 05_inventory_optimization.ipynb
│
├── reports/
│   ├── business_problem.md
│   ├── project_overview.md
│   ├── final_recommendations.md
│   └── etl_architecture.md
│
├── docs/
│   └── data_pipeline_flow.md
│
├── powerbi_dashboard/
│   └── Retail_Inventory_Dashboard.pbix
│
├── screenshots/
│   ├── dashboard.png
│   ├── sql_queries.png
│   ├── forecasting_model_output.png
│   └── stockout_model_output.png
│
├── logs/
│   └── pipeline.log
│
├── archive/
│   ├── processed/
│   └── logs/
│
├── models/
│   ├── stockout_classifier.pkl
│   └── demand_forecast_model_sample.pkl
│
├── .env
├── .gitignore
├── config.py
├── requirements.txt
├── README.md
└── run_pipeline.bat