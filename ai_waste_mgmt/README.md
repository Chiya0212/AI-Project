# AI-powered Waste Management System for Smart Cities

A smart waste management system built using **Python**, **AI/ML**, **Streamlit**, and **CSV-based data storage**. This project aims to help smart cities predict the amount of waste collected in different zones and optimize collection routes/resources accordingly.

---

## Features

- Predict waste generation using machine learning
- Analyze data trends like population, complaints, traffic, weather, and waste type
- Streamlit-based interactive web interface
- Uses CSV file as a mini-database (with 500 records)
- Pre-trained AI model using Random Forest Regressor

---

## Project Structure

```
ai_waste_mgmt/
│
├── waste_data.csv                 # Main dataset with 500 entries
├── model/
│   └── waste_predictor.pkl       # Trained machine learning model
├── src/
│   ├── train_model.py            # Model training script
│   └── predict.py                # Prediction logic
├── app/
│   └── main_app.py               # Streamlit frontend app
├── utils/
│   └── preprocessing.py          # (Optional) Utility functions for future expansion
├── requirements.txt              # Python dependencies
└── README.md                     # Project overview and instructions
```

---

## CSV Columns (waste_data.csv)

| Column Name         | Description                              |
|---------------------|------------------------------------------|
| Area_Code           | Unique area ID                           |
| Area_Name           | Name of the zone or locality             |
| Date                | Date of data entry                       |
| Waste_Collected_kg  | Amount of waste collected (target value) |
| Population          | Population of the area                   |
| Waste_Type          | Type of waste (Organic, Plastic, etc.)   |
| Weather             | Weather condition (Sunny, Rainy, etc.)   |
| Traffic_Level       | Road condition (Low, Medium, High)       |
| Complaint_Count     | Number of complaints registered          |

---

## AI Model

- **Type**: Regression
- **Algorithm**: Random Forest Regressor
- **Input Features**: Encoded values of population, waste type, weather, traffic, complaints
- **Target**: `Waste_Collected_kg`

---

## How to Run Locally

### Clone or Download

```bash
git clone https://github.com/yourusername/ai-waste-management.git
cd ai-waste-management
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Train the Model

```bash
python src/train_model.py
```

### Launch Streamlit App

```bash
streamlit run app/main_app.py
```

---

## Future Enhancements

- Time-series forecasting (ARIMA/LSTM)
- Live map dashboard with bin tracking
- Admin login and role-based dashboards
- Notifications to collection teams
- Integration with IoT bin sensors

---

## License

This project is open-source and free to use under the MIT License.

---

## Contributing

If you have suggestions, ideas, or improvements, feel free to raise an issue or submit a pull request.

---

## Author

**Chiya Nandeshwar**  
**Triveni Patle**  
Project for academic learning and smart city development.
