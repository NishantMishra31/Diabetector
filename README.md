
# 🩺 Diabetector – Diabetes Prediction Web App

**Diabetector** is a machine learning-powered web application that predicts the likelihood of diabetes based on user-provided health metrics. Built with Flask and deployed on Render, it offers a seamless interface for real-time risk assessment.

🔗 **Live Demo**: [https://diabetector.onrender.com](https://diabetector.onrender.com)

## 📌 Features

* 🎯 **Accurate Predictions**: Utilizes a Random Forest Classifier trained on the PIMA Indian Diabetes dataset.
* 🖥️ **User-Friendly Interface**: Intuitive frontend built with HTML and CSS.
* 🔁 **Real-Time Results**: Immediate feedback upon form submission.
* 🌐 **Deployed on Render**: Accessible anytime via the provided URL.

## 🧪 Input Parameters

The model requires the following health parameters:

* **Pregnancies**: Number of times pregnant
* **Glucose**: Plasma glucose concentration
* **Blood Pressure**: Diastolic blood pressure (mm Hg)
* **Skin Thickness**: Triceps skinfold thickness (mm)
* **Insulin**: 2-Hour serum insulin (mu U/ml)
* **BMI**: Body mass index (weight in kg/(height in m)^2)
* **Diabetes Pedigree Function**: A function that scores likelihood of diabetes based on family history
* **Age**: Age in years

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* pip

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/nishantmishra31/diabetector.git
   cd diabetector
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:

   ```bash
   python app.py
   ```

4. **Access the app**:
   Open your browser and navigate to `http://localhost:5000`

---

## 🛠️ Project Structure

```
diabetector/
├── app.py
├── train_model.py
├── model.pkl
├── diabetes.csv
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   └── index.html
```

* `app.py`: Flask application script
* `train_model.py`: Script to train and save the Random Forest model
* `model.pkl`: Serialized trained model
* `diabetes.csv`: Dataset used for training
* `requirements.txt`: Python dependencies
* `static/`: Contains CSS files
* `templates/`: Contains HTML templates

---

## 📊 Model Details

* **Algorithm**: Random Forest Classifier
* **Dataset**: PIMA Indian Diabetes dataset
* **Performance**: Achieved high accuracy on test data (specific metrics can be added here)

## 🌐 Deployment

The application is deployed on Render. Visit the live app here:

👉 [https://diabetector.onrender.com](https://diabetector.onrender.com)

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Author - Nishant Mishra (NishantMishra31)
© 2025 Nishant Mishra. All rights reserved.

