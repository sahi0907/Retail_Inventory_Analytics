import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load inventory data
df = pd.read_csv("data/cleaned/inventory_cleaned.csv")

# Create target column
df["StockoutRisk"] = (df["Inventory Level"] < df["Units Sold"]).astype(int)

# Select features
features = [
    "Inventory Level",
    "Units Sold",
    "Units Ordered",
    "Demand Forecast",
    "Price",
    "Discount"
]

# Keep only available columns
features = [col for col in features if col in df.columns]

X = df[features]
y = df["StockoutRisk"]

# Remove missing values
data = pd.concat([X, y], axis=1).dropna()

# Faster sample
data = data.sample(min(30000, len(data)), random_state=42)

X = data[features]
y = data["StockoutRisk"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=20,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "models/stockout_classifier.pkl")

print("Stockout model saved")