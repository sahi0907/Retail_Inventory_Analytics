import pandas as pd

# Load inventory data
df = pd.read_csv("data/cleaned/inventory_cleaned.csv")

# Create reorder point
df["ReorderPoint"] = (
    df["Demand Forecast"] * 1.2
)

# Identify products needing reorder
df["NeedReorder"] = (
    df["Inventory Level"] < df["ReorderPoint"]
).astype(int)

# Suggested reorder quantity
df["RecommendedOrderQty"] = (
    df["ReorderPoint"] - df["Inventory Level"]
)

# Avoid negative reorder quantity
df["RecommendedOrderQty"] = df["RecommendedOrderQty"].clip(lower=0)

# Keep only required rows
reorder_df = df[df["NeedReorder"] == 1]

# Save output
reorder_df.to_csv(
    "data/processed/reorder_recommendations.csv",
    index=False
)

print(reorder_df.head())
print("Reorder recommendations saved")