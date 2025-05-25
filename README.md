# 🩺 Diabetector — Instant Diabetes Risk Prediction Web App

**Diabetector** is an end-to-end machine learning-powered web application that helps users assess their diabetes risk instantly by entering key clinical indicators. It blends data science, healthcare, and responsive web development into a simple, informative, and mobile-friendly tool.

🚀 [Live App](https://diabetector.onrender.com) • 🧠 [Codebase](https://github.com/nishantmishra31/diabetector)

## 🧩 Features

- **Real-Time Prediction**  
  Enter real health data and receive an immediate diagnosis: *Diabetic* or *Non-Diabetic*.

- **ML Model Powered by Real Dataset**  
  Trained on the [PIMA Indian Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database), using a Random Forest Classifier.

- **Clean & Responsive UI**  
  Works seamlessly across desktop and mobile devices with real-time animations and scroll behavior.

- **Interactive Tooltips**  
  Info icons next to each field explain medical terms in simple language (fully mobile-compatible).

- **Analytics Integrated**  
  Google Analytics tracks site traffic and interaction to measure engagement.

- **One-Click Deploy with Render**  
  Publicly hosted Flask app with complete frontend-backend integration.

## 🧠 Input Parameters

| Parameter         | Description                                  |
|------------------|----------------------------------------------|
| **Pregnancies**   | Number of times the user has been pregnant   |
| **Glucose**       | Plasma glucose concentration (mg/dL)         |
| **Blood Pressure**| Diastolic blood pressure (mm Hg)             |
| **Skin Thickness**| Triceps skinfold thickness (mm)              |
| **Insulin**       | 2-hour serum insulin (mu U/ml)               |
| **BMI**           | Body Mass Index (kg/m²)                      |
| **DPF**           | Diabetes Pedigree Function (genetic risk)    |
| **Age**           | Age in years                                 |

## 🛠️ Tech Stack

| Layer        | Technologies              |
|--------------|---------------------------|
| **Frontend** | HTML, CSS, JS (with tooltips and responsive layout) |
| **Backend**  | Python, Flask             |
| **ML Model** | Random Forest (scikit-learn) |
| **Deployment** | Render (free tier)      |
| **Analytics** | Google Analytics         |

## 📁 Project Structure

```

diabetector/
│
├── app.py               # Flask app and routes
├── model.pkl            # Trained ML model
├── train\_model.py       # Model training script
├── diabetes.csv         # Dataset (PIMA)
├── requirements.txt     # Dependencies
│
├── templates/
│   └── index.html       # Frontend HTML
│
├── static/
│   ├── style.css        # UI styles
│   └── script.js        # Form logic and prediction fetch

````

## 🚀 Getting Started Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nishantmishra31/diabetector.git
   cd diabetector
````

2. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask App**

   ```bash
   python app.py
   ```

4. **Open in Browser**
   Navigate to `http://127.0.0.1:5000` and start predicting!

````

## 🌐 Live App

> 🧪 Deployed at: [https://diabetector.onrender.com](https://diabetector.onrender.com)
> *(Allow a few seconds for it to wake up if using Render free tier)*

## 📈 Analytics

Google Analytics is integrated to track:

* Page views
* Form submission events
* User engagement

## ✨ Credits

* **Dataset**: [PIMA Indian Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
* **Developer**: [Nishant Mishra](https://linkedin.com/in/nishantmishra31)
* **Tools**: Flask, scikit-learn, HTML, CSS, Render, GitHub

## 🤝 Contributing

Suggestions, issues, and pull requests are welcome!
If you’d like to collaborate, feel free to connect via [LinkedIn](https://linkedin.com/in/nishant-mishra-) or email to mnishant.work@gmail.com

## 🌟 Show Your Support

If you found this project helpful, give it a ⭐ on GitHub — and feel free to share it!

## Author- Nishant Mishra (NishantMishra31)

© 2025 Nishant Mishra. All rights reserved.


