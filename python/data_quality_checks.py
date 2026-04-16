import pandas as pd
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

sales_df = pd.read_csv("data/cleaned/sales_cleaned.csv")

missing_store = sales_df["Store"].isnull().sum()
negative_sales = (sales_df["Sales"] < 0).sum()
duplicates = sales_df.duplicated().sum()

logging.info(f"Missing Store IDs: {missing_store}")
logging.info(f"Negative Sales Rows: {negative_sales}")
logging.info(f"Duplicate Rows: {duplicates}")

if missing_store == 0 and negative_sales == 0:
    logging.info("Data quality passed")
else:
    logging.error("Data quality issues found")

print("Log file created: logs/pipeline.log")

sales_df = pd.read_csv("data/cleaned/sales_cleaned.csv")

# Check missing store IDs
missing_store = sales_df["Store"].isnull().sum()

# Check negative sales
negative_sales = (sales_df["Sales"] < 0).sum()

# Check duplicate rows
duplicates = sales_df.duplicated().sum()

print("Data Quality Report")
print("-------------------")
print(f"Missing Store IDs: {missing_store}")
print(f"Negative Sales Rows: {negative_sales}")
print(f"Duplicate Rows: {duplicates}")

if missing_store == 0 and negative_sales == 0:
    print("Data quality passed")
else:
    print("Data quality issues found")