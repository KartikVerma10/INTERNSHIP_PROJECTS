# 💳 Loan Prediction System

A Machine Learning-based web application that predicts whether a loan application is likely to be approved based on an applicant's financial and personal information.

The application is developed using **Flask** for the web interface and **K-Nearest Neighbors (KNN)** for prediction.

---

# 📌 Features

- Predicts loan approval status
- Built using the K-Nearest Neighbors (KNN) algorithm
- User-friendly web interface
- Data preprocessing using Label Encoding and Standard Scaling
- Instant prediction results
- Responsive design
- Fast and accurate predictions

---

# 🛠️ Tech Stack

- Python 3.11.5
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML5
- CSS3
- Pickle

---

# 🤖 Machine Learning Algorithm

### Model Used

- K-Nearest Neighbors (KNN) Classifier

### Data Preprocessing

- Label Encoding
- Standard Scaling

---

# 📂 Project Structure

```text
Loan_prediction/
│
├── dataset/
│   └── credit_risk_dataset.csv
│
├── model/
│   ├── default_encoder.pkl
│   ├── grade_encoder.pkl
│   ├── home_encoder.pkl
│   ├── intent_encoder.pkl
│   ├── model_credit.pkl
│   └── scaler.pkl
│
├── Notebook/
│   └── training_dataset.ipynb
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── architecture.png
├── app.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

The project uses a Credit Risk dataset containing applicant information.

### Features

- Person Age
- Person Income
- Home Ownership
- Employment Length
- Loan Intent
- Loan Grade
- Loan Amount
- Loan Interest Rate
- Loan Percentage Income
- Credit History Length
- Previous Loan Default

### Target

- Loan Approval Prediction

---

# ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Loan_prediction.git
```

### 2. Navigate to the Project Folder

```bash
cd Loan_prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Required Packages

```bash
pip install -r requirements.txt
```

### 6. Run the Flask Application

```bash
python app.py
```

### 7. Open in Browser

```text
http://127.0.0.1:5000/
```

---

# 🚀 Working Flow

```text
User Inputs Loan Details
            │
            ▼
      HTML Form (index.html)
            │
            ▼
       Flask Backend
            │
            ▼
      Label Encoding
            │
            ▼
     Standard Scaling
            │
            ▼
 K-Nearest Neighbors (KNN)
            │
            ▼
  Loan Approval Prediction
            │
            ▼
    Result Page (result.html)
```

---

# 🧠 How It Works

1. The user enters loan applicant details through the web form.
2. Flask receives the submitted data.
3. Categorical values are converted using saved Label Encoders.
4. Numerical values are standardized using the trained Scaler.
5. The processed data is passed to the trained KNN model.
6. The model predicts whether the loan is approved.
7. The prediction is displayed on the result page.

---

# 🏗️ Project Architecture

The Loan Prediction System follows a Machine Learning pipeline where user inputs are collected through a Flask web application, preprocessed using Label Encoding and Standard Scaling, and then passed to a trained **K-Nearest Neighbors (KNN)** model to predict loan approval.

## Architecture Diagram

---

<img width="1535" height="1024" alt="Image" src="https://github.com/user-attachments/assets/af8f6c7b-cfc0-4f09-9a4c-274f9bc49e6c" />

 

---

## Prediction Workflow

```text
                           +----------------+
                           |     User       |
                           +-------+--------+
                                   │
                                   ▼
                    +---------------------------+
                    | Frontend (HTML + CSS)     |
                    | index.html                |
                    +------------+--------------+
                                 │
                                 ▼
                    +---------------------------+
                    | Flask Backend (app.py)    |
                    +------------+--------------+
                                 │
                +----------------+----------------+
                │                                 │
                ▼                                 ▼
      Label Encoding                     Standard Scaling
(default_encoder.pkl, etc.)              (scaler.pkl)
                \                                 /
                 \                               /
                  +-------------+---------------+
                                │
                                ▼
                K-Nearest Neighbors (KNN)
                     model_credit.pkl
                                │
                                ▼
                 Loan Approval Prediction
                                │
                                ▼
                   result.html (Prediction)
```

---

## Model Training Pipeline

```text
credit_risk_dataset.csv
            │
            ▼
     Data Preprocessing
            │
            ▼
      Label Encoding
            │
            ▼
     Standard Scaling
            │
            ▼
      Train-Test Split
            │
            ▼
 Train K-Nearest Neighbors Model
            │
            ▼
     Model Evaluation
            │
            ▼
 Save Model, Scaler & Encoders
       (.pkl Files)
```

---

## Architecture Components

| Component | Description |
|-----------|-------------|
| **Frontend** | Collects loan applicant information through an HTML form. |
| **Flask Backend** | Receives user input, preprocesses the data, loads the trained model, and returns predictions. |
| **Label Encoders** | Convert categorical values into numerical format for the model. |
| **Standard Scaler** | Standardizes numerical features before prediction. |
| **KNN Classifier** | Predicts whether the loan application is approved. |
| **Result Page** | Displays the final prediction to the user. |

---

# 📷 Application Screenshots

## Home Page

(Add Screenshot Here)

## Prediction Result

(Add Screenshot Here)

---

# 📦 Requirements

- Python 3.11.5
- Flask
- NumPy
- Pandas
- Scikit-learn
- Pickle

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 📈 Future Improvements

- Deploy using Render or Railway
- Add prediction confidence score
- Improve UI with Bootstrap
- Add user authentication
- Store prediction history
- Compare multiple Machine Learning models
- Add REST API support

---

# 👨‍💻 Author

**Manas Sharma**

Engineering Student | Machine Learning Enthusiast

**GitHub:** https://github.com/ManasDevHub00

**LinkedIn:** https://www.linkedin.com/in/manas-sharma-68883b32a/

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub. Your support helps motivate future improvements and open-source contributions!