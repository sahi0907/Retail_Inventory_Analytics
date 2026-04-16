import pandas as pd
from config import *

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

sales_df = pd.read_csv("data/cleaned/sales_cleaned.csv")
inventory_df = pd.read_csv("data/cleaned/inventory_cleaned.csv")

# Prepare sales staging table
sales_stage = sales_df[[
    "Store",
    "Date",
    "Sales",
    "Customers",
    "Open",
    "Promo",
    "StateHoliday",
    "SchoolHoliday"
]]

sales_stage.columns = [
    "store_id",
    "date",
    "sales",
    "customers",
    "open",
    "promo",
    "state_holiday",
    "school_holiday"
]

# Prepare inventory staging table
inventory_stage = inventory_df[[
    "Product ID",
    "Store ID",
    "Inventory Level",
    "Units Sold",
    "Demand Forecast"
]]

inventory_stage.columns = [
    "product_id",
    "store_id",
    "inventory_level",
    "units_sold",
    "demand_forecast"
]

# Load to PostgreSQL staging tables
sales_stage.to_sql(
    "staging_sales",
    engine,
    if_exists="replace",
    index=False
)

inventory_stage.to_sql(
    "staging_inventory",
    engine,
    if_exists="replace",
    index=False
)

print("Staging tables loaded successfully")