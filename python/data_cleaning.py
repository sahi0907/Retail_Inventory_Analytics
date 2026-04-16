import pandas as pd

# Load datasets
sales_df = pd.read_csv("data/raw/sales.csv")
stores_df = pd.read_csv("data/raw/stores.csv")
walmart_df = pd.read_csv("data/raw/walmart.csv")
inventory_df = pd.read_csv("data/raw/inventory.csv")

# Display first 5 rows
print("Sales Data")
print(sales_df.head())

print("\nStores Data")
print(stores_df.head())

print("\nWalmart Data")
print(walmart_df.head())

print("\nInventory Data")
print(inventory_df.head())


import pandas as pd

# Load datasets
sales_df = pd.read_csv("data/raw/sales.csv")
stores_df = pd.read_csv("data/raw/stores.csv")
walmart_df = pd.read_csv("data/raw/walmart.csv")
inventory_df = pd.read_csv("data/raw/inventory.csv")

#Sales Data
sales_df.drop_duplicates(inplace=True)

sales_df["Date"] = pd.to_datetime(sales_df["Date"])

sales_df["Open"] = sales_df["Open"].fillna(1)
sales_df["Promo"] = sales_df["Promo"].fillna(0)
sales_df["StateHoliday"] = sales_df["StateHoliday"].fillna("0")
sales_df["SchoolHoliday"] = sales_df["SchoolHoliday"].fillna(0)

#Stores data
stores_df.drop_duplicates(inplace=True)

stores_df["CompetitionDistance"] = stores_df["CompetitionDistance"].fillna(
    stores_df["CompetitionDistance"].median()
)

stores_df["CompetitionOpenSinceMonth"] = stores_df["CompetitionOpenSinceMonth"].fillna(0)
stores_df["CompetitionOpenSinceYear"] = stores_df["CompetitionOpenSinceYear"].fillna(0)
stores_df["Promo2SinceWeek"] = stores_df["Promo2SinceWeek"].fillna(0)
stores_df["Promo2SinceYear"] = stores_df["Promo2SinceYear"].fillna(0)
stores_df["PromoInterval"] = stores_df["PromoInterval"].fillna("None")

# Walmart Data
walmart_df.drop_duplicates(inplace=True)

if "Date" in walmart_df.columns:
    walmart_df["Date"] = pd.to_datetime(walmart_df["Date"], dayfirst=True)
  

walmart_df = walmart_df.ffill()

#Inventory Data
inventory_df.drop_duplicates(inplace=True)

inventory_df = inventory_df.ffill()

# Save cleaned datasets
sales_df.to_csv("data/cleaned/sales_cleaned.csv", index=False)
stores_df.to_csv("data/cleaned/stores_cleaned.csv", index=False)
walmart_df.to_csv("data/cleaned/walmart_cleaned.csv", index=False)
inventory_df.to_csv("data/cleaned/inventory_cleaned.csv", index=False)

print("Cleaned files saved in data/cleaned/")