import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import random

# Simulated dataset with features common in chronic disease prediction
data = pd.DataFrame({
    'age': np.random.randint(30, 80, 100),
    'bmi': np.random.uniform(18, 40, 100),
    'blood_pressure': np.random.randint(90, 180, 100),
    'glucose': np.random.randint(70, 200, 100),
    'activity_level': np.random.randint(1, 5, 100),  # 1: low, 5: high
    'risk': np.random.randint(0, 2, 100)  # 0: low risk, 1: high risk
})

# Feature matrix and labels
X = data.drop('risk', axis=1)
y = data['risk']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred)
print("\n📊 Model Performance:\n")
print(report)

# Simulate a patient input
new_patient = pd.DataFrame([{
    'age': 55,
    'bmi': 29.5,
    'blood_pressure': 145,
    'glucose': 160,
    'activity_level': 2
}])

# Predict risk
risk_prediction = model.predict(new_patient)[0]
risk_proba = model.predict_proba(new_patient)[0][1]

# Chatbot simulation
def health_chatbot(risk_level):
    if risk_level == 1:
        return random.choice([
            " High risk detected. Please consult your doctor immediately.",
            " Reminder: It's time for your medication.",
            "Tip: Reduce salt/sugar intake. Stay active!"
        ])
    else:
        return random.choice([
            "Your health is stable. Keep it up!",
            " Stay active and hydrated!",
            " Balanced meals and exercise help keep you well."
        ])

# Output
print("\n🩺 New Patient Risk Prediction:")
print("Risk Level:", "High" if risk_prediction == 1 else "Low")
print(f"Probability of Risk: {risk_proba:.2f}")
print("💬 Chatbot says:", health_chatbot(risk_prediction))
