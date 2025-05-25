
# 🩺 Diabetector — Instant Diabetes Risk Prediction Web App powered by Machine Learning

**Diabetector** is a machine learning-powered web application that allows users to instantly assess their risk of diabetes based on real clinical health indicators. Built using Python, Flask, and a Random Forest model, it delivers fast, accessible predictions in a clean, responsive interface.

🚀 [Live App](https://diabetector.onrender.com) • 🧠 [Source Code](https://github.com/nishantmishra31/diabetector)

## 🧩 Features

- **Real-Time Prediction**  
  Enter real health data and receive an immediate diabetic/non-diabetic risk assessment.

- **ML Model Powered by Real Dataset**  
  Trained on the **PIMA Indian Diabetes Dataset**, a trusted dataset in the medical and ML community.

- **Clean & Responsive UI**  
  Built with HTML and CSS to ensure a seamless experience across desktop and mobile devices.

- **Full-Stack Integration**  
  Flask handles both the backend prediction logic and frontend routing in a single service.

- **Fully Deployed on Render**  
  Publicly available and cloud-hosted with a free-tier deployment setup.

---

## 📊 Input Parameters

The app takes the following medical inputs:

| Parameter         | Description                                 |
|------------------|---------------------------------------------|
| Pregnancies       | Number of pregnancies                       |
| Glucose           | Plasma glucose concentration                |
| Blood Pressure    | Diastolic blood pressure (mm Hg)            |
| Skin Thickness    | Triceps skinfold thickness (mm)             |
| Insulin           | 2-Hour serum insulin (mu U/ml)              |
| BMI               | Body mass index (kg/m²)                     |
| Diabetes Pedigree Function | Genetic diabetes likelihood factor |
| Age               | Age in years                                |

---

## 🧠 ML Model Details

- **Algorithm**: Random Forest Classifier
- **Dataset**: [PIMA Indian Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Library Stack**:
  - `scikit-learn`
  - `numpy`
  - `joblib`

---

## 🛠️ Tech Stack

| Layer        | Technology           |
|--------------|----------------------|
| Frontend     | HTML, CSS, JS        |
| Backend      | Python, Flask        |
| ML           | scikit-learn, joblib |
| Deployment   | Render               |

---

## 🚀 Getting Started Locally

### 1. Clone the Repository
```bash
git clone https://github.com/nishantmishra31/diabetector.git
cd diabetector
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

## 📁 Project Structure

```
diabetector/
│
├── app.py                  # Flask app and routes
├── model.pkl               # Trained Random Forest model
├── train_model.py          # Script to train the model
├── diabetes.csv            # Dataset used
├── requirements.txt        # Project dependencies
│
├── templates/
│   └── index.html          # Frontend UI
│
├── static/
│   └── style.css           # Stylesheet
│   └── favicon.ico         # Optional browser icon
```

---

## 🌐 Deployment Notes

* This app is hosted on [Render](https://render.com) with both the frontend and backend in a single web service.
* Free-tier deployments may take \~10 seconds to wake up.

## 📈 Analytics

Google Analytics is integrated to track user traffic and usage patterns. Events like form submissions are recorded for insights.

## 🙌 Acknowledgements

* Dataset: [Kaggle - PIMA Indian Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
* Flask, scikit-learn, Render, and the open-source community

## 🤝 Contributing

Pull requests and feature suggestions are welcome! Feel free to fork the repo and make it even better.

## ✨ Author

**Nishant Mishra**
Connect with me on [LinkedIn](https://linkedin.com/in/nishant-mishra-)

© 2025 Nishant Mishra. All rights reserved.


