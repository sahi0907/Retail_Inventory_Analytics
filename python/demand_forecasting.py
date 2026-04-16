import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load data
df = pd.read_csv("data/processed/final_featured_data.csv")

# Select useful features
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

# Keep only available columns
features = [col for col in features if col in df.columns]

X = df[features]
y = df["Sales"]

# Remove missing rows
data = pd.concat([X, y], axis=1).dropna()

X = data[features]
y = data["Sales"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Use smaller sample for quick testing
data = data.sample(50000, random_state=42)

X = data[features]
y = data["Sales"]

model = RandomForestRegressor(
    n_estimators=20,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Performance")
print(f"MAE: {mae:.2f}")
print(f"R2 Score: {r2:.4f}")

# Save model
joblib.dump(model, "models/demand_forecast_model.pkl")

print("Model saved in models/demand_forecast_model.pkl")