from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

model = joblib.load('model.pkl') # this loads the model using joblib

@app.route("/")
def home():
    return render_template("index.html") # flask renders html file here

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
    port = int(os.environ.get("PORT", 5000))  # this is done for local run
    app.run(host="0.0.0.0", port=port, debug=True)
