import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.predict import predict_waste

st.set_page_config(page_title="Smart Waste AI", layout="centered")

st.title("AI-Powered Waste Management System")

st.subheader("Enter Area Details")

with st.form("waste_input_form"):
    population = st.number_input("Population", min_value=100, max_value=1000000, value=1000)
    complaints = st.number_input("Number of Complaints", min_value=0, value=2)

    waste_type = st.selectbox("Waste Type", ["Organic", "Plastic", "E-Waste"])
    weather = st.selectbox("Weather", ["Cloudy", "Rainy", "Sunny"])
    traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])

    submit = st.form_submit_button("Predict Waste (kg)")
 
if submit:
    # Match only the columns used in training
    input_data = {
        "Population": population,
        "Complaint_Count": complaints,
        "Waste_Type_Organic": 1 if waste_type == "Organic" else 0,
        "Waste_Type_Plastic": 1 if waste_type == "Plastic" else 0,
        "Weather_Rainy": 1 if weather == "Rainy" else 0,
        "Weather_Sunny": 1 if weather == "Sunny" else 0,
        "Traffic_Level_Low": 1 if traffic == "Low" else 0,
        "Traffic_Level_Medium": 1 if traffic == "Medium" else 0,
        # Traffic_Level_High and Waste_Type_E-Waste were dropped during training!
    }

    predicted_kg = predict_waste(input_data) 
    st.success(f"Estimated Waste Collection: **{predicted_kg:.2f} kg**")
