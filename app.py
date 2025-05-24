from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load('model.pkl')

@app.route("/")
def home():
    return render_template("index.html")  # Renders index.html from /templates

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
    app.run(debug=True)
