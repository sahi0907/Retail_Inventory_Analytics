import pandas as pd

# Load datasets
sales_df = pd.read_csv("data/raw/sales.csv")
stores_df = pd.read_csv("data/raw/stores.csv")
walmart_df = pd.read_csv("data/raw/walmart.csv")
inventory_df = pd.read_csv("data/raw/inventory.csv")

datasets = {
    "Sales": sales_df,
    "Stores": stores_df,
    "Walmart": walmart_df,
    "Inventory": inventory_df
}

with open("reports/data_inspection_report.txt", "w", encoding="utf-8") as file:

    for name, df in datasets.items():
        file.write(f"\n{name} Dataset\n")
        file.write("=" * 50 + "\n")

        file.write("\nShape:\n")
        file.write(str(df.shape) + "\n")

        file.write("\nColumns:\n")
        file.write(str(df.columns.tolist()) + "\n")

        file.write("\nData Types:\n")
        file.write(str(df.dtypes) + "\n")

        file.write("\nMissing Values:\n")
        file.write(str(df.isnull().sum()) + "\n")

        file.write("\nDuplicate Rows:\n")
        file.write(str(df.duplicated().sum()) + "\n")

        file.write("\nFirst 5 Rows:\n")
        file.write(str(df.head()) + "\n\n")

print("Report created successfully: reports/data_inspection_report.txt")