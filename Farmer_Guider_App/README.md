# 🌱 Smart Farmer AI
### AI-Powered Crop & Fertilizer Recommendation System

Smart Farmer AI is a Machine Learning-based web application developed using **Python**, **Flask**, and **Scikit-learn**. The application helps farmers make informed agricultural decisions by recommending the most suitable crop and fertilizer based on soil nutrients and environmental conditions.

---

## 📌 Features

- 🌾 Crop Recommendation using Machine Learning
- 🧪 Fertilizer Recommendation
- 📊 Data Preprocessing using StandardScaler & LabelEncoder
- 💻 Interactive Flask Web Application
- 📱 Responsive and Professional User Interface
- ⚡ Fast and Accurate Predictions

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- Font Awesome

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Random Forest Classifier
- StandardScaler
- LabelEncoder
- Joblib

### Libraries
- NumPy
- Pandas

---

## 📂 Project Structure

```
Smart-Farmer-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── crop_recom_model.pkl
│   ├── crop_recom_scaler.pkl
│   ├── crop_recom_encoder.pkl
│   ├── fertilizer_rf_model.pkl
│   ├── fert_scaler.pkl
│   ├── fert_soil_encoder.pkl
│   ├── fert_crop_encoder.pkl
│   └── fert_target_encoder.pkl
│
├── templates/
│   ├── index.html
│   ├── crop.html
│   ├── fertilizer.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── dataset/
│   ├── Crop_recommendation.csv
│   └── Fertilizer Recommendation.csv
│
└── notebooks/
    ├── Crop_Model.ipynb
    └── Fertilizer_Model.ipynb
```

---

# 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Smart-Farmer-AI.git
```

Move into the project folder

```bash
cd Smart-Farmer-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000/
```

---

# 🌾 Crop Recommendation

The Crop Recommendation model predicts the most suitable crop based on the following parameters:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

### Machine Learning Algorithm

- Random Forest Classifier

---

# 🧪 Fertilizer Recommendation

The Fertilizer Recommendation model predicts the most suitable fertilizer using:

- Temperature
- Moisture
- Rainfall
- pH
- Nitrogen
- Phosphorous
- Potassium
- Carbon
- Soil Type
- Crop Type

### Machine Learning Algorithm

- Random Forest Classifier

---

# 📊 Workflow

```
Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Feature Engineering
     │
     ▼
Label Encoding
     │
     ▼
Feature Scaling
     │
     ▼
Model Training
     │
     ▼
Model Evaluation
     │
     ▼
Save Model (.pkl)
     │
     ▼
Flask Application
     │
     ▼
Prediction
```

---

# 📷 Application Modules

### 🏠 Home Page
- Navigation to Crop Recommendation
- Navigation to Fertilizer Recommendation

### 🌾 Crop Recommendation
- Soil parameter input form
- AI-based crop prediction

### 🧪 Fertilizer Recommendation
- Soil and crop information form
- AI-based fertilizer prediction

### 📈 Result Page
- Displays prediction result
- Option to predict again
- Return to Home

---

# 📌 Machine Learning Libraries

- Scikit-learn
- NumPy
- Pandas
- Joblib

---

# 🎯 Future Improvements

- Weather API Integration
- Soil Image Classification
- Crop Disease Detection
- Multi-language Support
- Fertilizer Dosage Recommendation
- Yield Prediction
- Cloud Deployment
- User Authentication

---

# 👨‍💻 Developed By

**Kartik Verma**

Machine Learning Intern

Developed as part of an internship project using **Python**, **Flask**, and **Machine Learning**.

---

# 📄 License

This project is intended for educational and learning purposes.

© 2026 Kartik Verma. All Rights Reserved.