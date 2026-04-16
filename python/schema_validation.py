import pandas as pd

sales_df = pd.read_csv("data/cleaned/sales_cleaned.csv")

required_columns = [
    "Store",
    "Date",
    "Sales",
    "Customers",
    "Promo"
]

missing_columns = []

for col in required_columns:
    if col not in sales_df.columns:
        missing_columns.append(col)

if len(missing_columns) == 0:
    print("Schema validation passed")
else:
    print("Missing columns:", missing_columns)