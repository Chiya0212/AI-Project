import joblib
import pandas as pd

# Load model
model = joblib.load(r"D:\Clg-workshop\Pro\ai_waste_mgmt\model\waste_predictor.pkl")

# Columns used during training (must match exactly)
expected_columns = [
    "Population", "Complaint_Count",
    "Waste_Type_Organic", "Waste_Type_Plastic",
    "Weather_Rainy", "Weather_Sunny",
    "Traffic_Level_Low", "Traffic_Level_Medium"
]

def prepare_input(user_input_dict):
    df = pd.DataFrame([user_input_dict])
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0  
    df = df[expected_columns]
    return df

def predict_waste(user_input_dict):
    input_df = prepare_input(user_input_dict)
    prediction = model.predict(input_df)
    return prediction[0]
