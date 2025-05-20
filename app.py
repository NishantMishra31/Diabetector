from flask import Flask, request, jsonify
from flask_cors import CORS 
import numpy as np
import joblib
import os  # <-- Added to read the PORT environment variable

app = Flask(__name__)
CORS(app)

# Load your model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "🚀 Diabetes Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    try:
        input_data = [
            data["Pregnancies"],
            data["Glucose"],
            data["BP"],
            data["SkinThickness"],
            data["Insulin"],
            data["BMI"],
            data["DPF"],
            data["Age"]
        ]
        input_np = np.array(input_data).reshape(1, -1)
        prediction = int(model.predict(input_np)[0])
        result = "Diabetic" if prediction == 1 else "Non-Diabetic"
        return jsonify({"prediction": result})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    # Render requires binding to 0.0.0.0 and using the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
