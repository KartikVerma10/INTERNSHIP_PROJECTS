from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model/model_credit.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

home_encoder = pickle.load(open("model/home_encoder.pkl", "rb"))
intent_encoder = pickle.load(open("model/intent_encoder.pkl", "rb"))
grade_encoder = pickle.load(open("model/grade_encoder.pkl", "rb"))
default_encoder = pickle.load(open("model/default_encoder.pkl", "rb"))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    
        
        person_age = float(request.form['person_age'])
        person_income = float(request.form['person_income'])
        person_emp_length = float(request.form['person_emp_length'])
        loan_amnt = float(request.form['loan_amnt'])
        loan_int_rate = float(request.form['loan_int_rate'])
        loan_percent_income = float(request.form['loan_percent_income'])
        cb_person_cred_hist_length = float(request.form['cb_person_cred_hist_length'])

       
        person_home_ownership = home_encoder.transform(
            [request.form['person_home_ownership']]
        )[0]

        loan_intent = intent_encoder.transform(
            [request.form['loan_intent']]
        )[0]

        loan_grade = grade_encoder.transform(
            [request.form['loan_grade']]
        )[0]

        cb_person_default_on_file = default_encoder.transform(
            [request.form['cb_person_default_on_file']]
        )[0]

        
        data = np.array([[ 
            person_age,
            person_income,
            person_emp_length,
            loan_amnt,
            loan_int_rate,
            loan_percent_income,
            cb_person_cred_hist_length,
            person_home_ownership,
            loan_intent,
            loan_grade,
            cb_person_default_on_file
        ]])

       
        data = scaler.transform(data)

        
        prediction = model.predict(data)[0]

        result = "Loan Approved" if prediction == 0 else "Loan Rejected"

        return render_template("result.html", result=result)

     


if __name__ == "__main__":
    app.run(debug=True)