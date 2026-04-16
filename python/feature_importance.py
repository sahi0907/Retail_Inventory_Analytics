import pandas as pd
import joblib

# Load data and model
df = pd.read_csv("data/processed/final_featured_data.csv")
model = joblib.load("models/demand_forecast_model.pkl")

features = [
    "Store",
    "DayOfWeek",
    "Promo",
    "SchoolHoliday",
    "Month",
    "Year",
    "CompetitionDistance",
    "CompetitionAge",
    "PromoDuration",
    "PreviousDaySales",
    "PreviousWeekSales",
    "Rolling7DaySales"
]

features = [col for col in features if col in df.columns]

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print(importance_df)

importance_df.to_csv(
    "data/processed/feature_importance.csv",
    index=False
)

print("Feature importance saved")