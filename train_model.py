import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib  

data = pd.read_csv("diabetes.csv")

data.rename(columns={'DiabetesPedigreeFunction': 'DPF', 'BloodPressure': 'BP'}, inplace=True)

for column in ['Glucose', 'BP', 'SkinThickness', 'Insulin', 'BMI', 'DPF', 'Age']:
    data[column] = data[column].replace(0, data[column].mean())

X = data.drop(columns=["Outcome"])
Y = data["Outcome"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, random_state=10)

model = RandomForestClassifier(random_state=10)
model.fit(X_train, Y_train.ravel())

pred = model.predict(X_test)
acc = metrics.accuracy_score(Y_test, pred)
print(f"Model Accuracy: {acc:.2f}")

joblib.dump(model, "model.pkl")
print("Model saved to model.pkl")

def predict_diabetes(input_data):
    """
    here input_data is given in form of a list or array in the order:
        [Pregnancies, Glucose, BP, SkinThickness, Insulin, BMI, DPF, Age]
    which returns: 0 or 1 predicting the diabetes
    """
    input_np = np.array(input_data).reshape(1, -1)
    return model.predict(input_np)[0]
