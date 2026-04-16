import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Root@localhost:5432/retail_inventory_db"
)

# Load processed datasets
sales_df = pd.read_csv("data/processed/final_featured_data.csv")
reorder_df = pd.read_csv("data/processed/reorder_recommendations.csv")

# Select columns matching retail_sales table
sales_table = sales_df[[
    "Store",
    "Date",
    "Sales",
    "Customers",
    "Open",
    "Promo",
    "StateHoliday",
    "SchoolHoliday",
    "StoreType",
    "Assortment",
    "CompetitionDistance",
    "CompetitionAge",
    "PromoDuration",
    "PreviousDaySales",
    "PreviousWeekSales",
    "Rolling7DaySales"
]]

sales_table.columns = [
    "store_id",
    "date",
    "sales",
    "customers",
    "open",
    "promo",
    "state_holiday",
    "school_holiday",
    "store_type",
    "assortment",
    "competition_distance",
    "competition_age",
    "promo_duration",
    "previous_day_sales",
    "previous_week_sales",
    "rolling_7day_sales"
]

# Inventory table
inventory_table = reorder_df[[
    "Product ID",
    "Store ID",
    "Inventory Level",
    "Units Sold",
    "Demand Forecast",
    "ReorderPoint",
    "RecommendedOrderQty",
    "NeedReorder"
]]

inventory_table.columns = [
    "product_id",
    "store_id",
    "inventory_level",
    "units_sold",
    "demand_forecast",
    "reorder_point",
    "recommended_order_qty",
    "need_reorder"
]

# Load into PostgreSQL
sales_table.to_sql(
    "retail_sales",
    engine,
    if_exists="replace",
    index=False
)

inventory_table.to_sql(
    "inventory_recommendations",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into PostgreSQL")