import pandas as pd

# Load cleaned files
sales_df = pd.read_csv("data/cleaned/sales_cleaned.csv")
stores_df = pd.read_csv("data/cleaned/stores_cleaned.csv")
walmart_df = pd.read_csv("data/cleaned/walmart_cleaned.csv")
inventory_df = pd.read_csv("data/cleaned/inventory_cleaned.csv")

#convert dates 
sales_df["Date"] = pd.to_datetime(sales_df["Date"])
walmart_df["Date"] = pd.to_datetime(walmart_df["Date"], format="mixed")

#Merge sales with store information 
merged_df = sales_df.merge(stores_df, on="Store", how="left")

#merge with walmart external factors 
if "Store" in walmart_df.columns:
    merged_df = merged_df.merge(
        walmart_df,
        on=["Store", "Date"],
        how = "left",
        suffixes = ("", "_walmart")
    )

#Save merge data 
merged_df.to_csv("data/processed/final_merge_data.csv", index = False)

print("Merged dataset created succesfully")
print("shape:", merged_df.shape)
print(merged_df.head())