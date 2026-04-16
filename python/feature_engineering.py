import pandas as pd

# Load merged data
df = pd.read_csv("data/processed/final_merge_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Date Features
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["DayOfWeek"] = df["Date"].dt.dayofweek
df["WeekOfYear"] = df["Date"].dt.isocalendar().week
df["Quarter"] = df["Date"].dt.quarter
df["IsWeekend"] = df["DayOfWeek"].isin([5, 6]).astype(int)

# Competition Age
df["CompetitionAge"] = (
    df["Year"] - df["CompetitionOpenSinceYear"]
)

# Promo Duration
df["PromoDuration"] = (
    df["Year"] - df["Promo2SinceYear"]
)

# Fill negative values if any
df["CompetitionAge"] = df["CompetitionAge"].clip(lower=0)
df["PromoDuration"] = df["PromoDuration"].clip(lower=0)

# Lag features
df = df.sort_values(["Store", "Date"])

df["PreviousDaySales"] = df.groupby("Store")["Sales"].shift(1)
df["PreviousWeekSales"] = df.groupby("Store")["Sales"].shift(7)

# Rolling Average
df["Rolling7DaySales"] = (
    df.groupby("Store")["Sales"]
    .rolling(7)
    .mean()
    .reset_index(level=0, drop=True)
)

# Fill missing lag values
df["PreviousDaySales"] = df["PreviousDaySales"].fillna(0)
df["PreviousWeekSales"] = df["PreviousWeekSales"].fillna(0)
df["Rolling7DaySales"] = df["Rolling7DaySales"].fillna(0)

# Save final feature engineered data
df.to_csv("data/processed/final_featured_data.csv", index=False)

print("Feature engineering completed")
print(df.head())