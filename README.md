# Diabetes Prediction Using Random Forest Classifier

**Diabetector** is a machine learning-based application designed to predict the likelihood of diabetes in an individual using medical diagnostic data. It employs a Random Forest Classifier to analyze key health indicators and classify whether a person is likely to be diabetic or not.

## 🧠 How It Works

1. **Data Ingestion**: The application reads the diabetes dataset (`diabetes.csv`) containing various medical features such as glucose level, BMI, insulin, age, etc.

2. **Preprocessing**:

   * Cleans missing or zero values in key features.
   * Normalizes and structures the data for model training.

3. **Model Training**:

   * Uses a **Random Forest Classifier** from `scikit-learn`.
   * The dataset is split into training and test sets (typically 80/20).
   * The model is trained to distinguish patterns between diabetic and non-diabetic individuals.

4. **Prediction**:

   * The user inputs health parameters through the command line.
   * The model returns a binary result: either **Diabetic** or **Non-Diabetic**.

5. **Visualization**:

   * Optional graphs show feature importance and data distribution using `matplotlib` and `seaborn`.

## 🚀 Features

* Clean and structured dataset processing
* Accurate predictions using ensemble learning
* Simple user interface for entering health data
* Modular, beginner-friendly Python code
* Extensible for GUI or web deployment

## 🛠️ Technologies Used

| Tool         | Purpose                          |
| ------------ | -------------------------------- |
| Python       | Core language                    |
| Pandas       | Data manipulation                |
| NumPy        | Numerical operations             |
| Scikit-learn | Machine learning (Random Forest) |
| Matplotlib   | Data visualization               |
| Seaborn      | Statistical plotting             |

## 📦 Installation

# Clone the repo
git clone https://github.com/NishantMishra31/Diabetector.git
cd Diabetector

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r Requirements.txt

## ▶️ Running the Application

python "Diabetes Predicition System.py"

* You’ll be prompted to input values such as:

  * Glucose level
  * BMI (Body Mass Index)
  * Age
  * Insulin level
  * Skin thickness, Blood pressure, etc.

* The program will then output a prediction.

## 📁 Dataset

The dataset used is based on the **Pima Indians Diabetes Database**. It includes 768 rows and 9 columns of data on women of Pima Indian heritage aged 21 and older.

| Feature                  | Description                       |
| ------------------------ | --------------------------------- |
| Pregnancies              | Number of times pregnant          |
| Glucose                  | Plasma glucose concentration      |
| BloodPressure            | Diastolic blood pressure (mm Hg)  |
| SkinThickness            | Triceps skin fold thickness (mm)  |
| Insulin                  | 2-Hour serum insulin (mu U/ml)    |
| BMI                      | Body mass index (weight in kg/m²) |
| DiabetesPedigreeFunction | Genetic propensity                |
| Age                      | Age in years                      |
| Outcome                  | 1 if diabetic, 0 otherwise        |

## Future Improvements

- **Hyperparameter Tuning:** Improve the model’s performance by fine-tuning parameters.
- **Testing with Other Models:** Compare performance with other algorithms such as SVM, Logistic Regression, and Neural Networks.
- **Larger Datasets:** Expanding the dataset to include more features and records could enhance the model's accuracy and generalizability.

## Contributing

If you want to contribute to this project, feel free to submit issues or pull requests. Any suggestions or improvements are welcome.

1. Fork the repo.
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Open a pull request.

## 🙏 Acknowledgments

* The creators of the Pima Indians Diabetes Dataset
* The open-source community for libraries and support
