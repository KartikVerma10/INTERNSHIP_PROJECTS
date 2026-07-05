from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# ==========================================================
# Base Directory
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# ==========================================================
# Load Crop Recommendation Model
# ==========================================================

try:
    crop_model = joblib.load(os.path.join(MODEL_DIR, "crop_recom_model.pkl"))
    crop_scaler = joblib.load(os.path.join(MODEL_DIR, "crop_recom_scaler.pkl"))
    crop_encoder = joblib.load(os.path.join(MODEL_DIR, "crop_recom_encoder.pkl"))

    print("✅ Crop Recommendation Model Loaded")

except Exception as e:
    crop_model = None
    print("❌ Crop Model Error:", e)

# ==========================================================
# Load Fertilizer Recommendation Model
# ==========================================================

try:
    fert_model = joblib.load(os.path.join(MODEL_DIR, "fertilizer_rf_model.pkl"))
    fert_scaler = joblib.load(os.path.join(MODEL_DIR, "fert_scaler.pkl"))
    fert_soil_encoder = joblib.load(os.path.join(MODEL_DIR, "fert_soil_encoder.pkl"))
    fert_crop_encoder = joblib.load(os.path.join(MODEL_DIR, "fert_crop_encoder.pkl"))
    fert_target_encoder = joblib.load(os.path.join(MODEL_DIR, "fert_target_encoder.pkl"))

    print("✅ Fertilizer Recommendation Model Loaded")

except Exception as e:
    fert_model = None
    print("❌ Fertilizer Model Error:", e)

# ==========================================================
# Home Page
# ==========================================================

@app.route("/")
def home():
    return render_template("index.html")

# ==========================================================
# Crop Recommendation Page
# ==========================================================

@app.route("/crop")
def crop():
    return render_template("crop.html")

# ==========================================================
# Fertilizer Recommendation Page
# ==========================================================

@app.route("/fertilizer")
def fertilizer():
    return render_template("fertilizer.html")

# ==========================================================
# Crop Prediction
# ==========================================================

@app.route("/predict_crop", methods=["POST"])
def predict_crop():

    if crop_model is None:
        return render_template(
            "result.html",
            prediction="Crop Recommendation Model Not Loaded!",
            prediction_type="error"
        )

    try:

        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        features = np.array([[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]])

        features = crop_scaler.transform(features)

        prediction = crop_model.predict(features)

        crop_name = crop_encoder.inverse_transform(prediction)[0]

        return render_template(
            "result.html",
            prediction=crop_name.title(),
            prediction_type="crop"
        )

    except Exception as e:

        return render_template(
            "result.html",
            prediction=str(e),
            prediction_type="error"
        )

# ==========================================================
# Fertilizer Prediction
# ==========================================================

@app.route("/predict_fertilizer", methods=["POST"])
def predict_fertilizer():

    if fert_model is None:
        return render_template(
            "result.html",
            prediction="Fertilizer Recommendation Model Not Loaded!",
            prediction_type="error"
        )

    try:

        temperature = float(request.form["Temperature"])
        moisture = float(request.form["Moisture"])
        rainfall = float(request.form["Rainfall"])
        ph = float(request.form["PH"])

        nitrogen = float(request.form["Nitrogen"])
        phosphorous = float(request.form["Phosphorous"])
        potassium = float(request.form["Potassium"])
        carbon = float(request.form["Carbon"])

        soil = request.form["Soil"]
        crop = request.form["Crop"]

        soil_encoded = fert_soil_encoder.transform([soil])[0]
        crop_encoded = fert_crop_encoder.transform([crop])[0]

        features = np.array([[
            temperature,
            moisture,
            rainfall,
            ph,
            nitrogen,
            phosphorous,
            potassium,
            carbon,
            soil_encoded,
            crop_encoded
        ]])

        features = fert_scaler.transform(features)

        prediction = fert_model.predict(features)

        fertilizer_name = fert_target_encoder.inverse_transform(prediction)[0]

        return render_template(
            "result.html",
            prediction=fertilizer_name,
            prediction_type="fertilizer"
        )

    except Exception as e:

        return render_template(
            "result.html",
            prediction=str(e),
            prediction_type="error"
        )

# ==========================================================
# Run Flask App
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)