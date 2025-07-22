import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load Data
data = pd.read_csv("waste_data.csv")

# Drop non-numeric ID and names
data = data.drop(columns=["Date", "Area_Name", "Area_Code"])

# One-hot encode categorical columns
data = pd.get_dummies(data, columns=["Waste_Type", "Weather", "Traffic_Level"], drop_first=True)

# Separate input/output
X = data.drop(["Waste_Collected_kg"], axis=1)
y = data["Waste_Collected_kg"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Save model (use raw string)
joblib.dump(model, r"D:\Clg-workshop\Pro\ai_waste_mgmt\model\waste_predictor.pkl")
