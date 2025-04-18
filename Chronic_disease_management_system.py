import pandas as pd
import numpy as np

def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            val = float(input(prompt))
            if min_val <= val <= max_val:
                return val
            else:
                print(f"Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def predict_risk(age, bmi, systolic_bp, diastolic_bp, cholesterol, glucose):
    # Simple risk calculation using a weighted sum (dummy logic)
    risk_score = (
        0.2 * age +
        0.3 * bmi +
        0.1 * systolic_bp +
        0.1 * diastolic_bp +
        0.2 * cholesterol / 3 +
        0.1 * glucose / 5
    )
    # Normalize to 1–10 scale
    risk_score = min(10, max(1, risk_score / 10))
    return round(risk_score, 2)

def main():
    print("Welcome to the AI-Powered Chronic Disease Risk Predictor")
    age = get_valid_input("Enter your age (1-100): ", 1, 100)
    bmi = get_valid_input("Enter your BMI (20-40): ", 20, 40)
    systolic_bp = get_valid_input("Enter your systolic blood pressure (70-200): ", 70, 200)
    diastolic_bp = get_valid_input("Enter your diastolic blood pressure (50-150): ", 50, 150)
    cholesterol = get_valid_input("Enter your cholesterol level (150-300): ", 150, 300)
    glucose = get_valid_input("Enter your glucose level (50-500): ", 50, 500)

    risk = predict_risk(age, bmi, systolic_bp, diastolic_bp, cholesterol, glucose)
    print(f"Predicted Chronic Disease Risk Score (1-10): {risk}")

if __name__ == "__main__":
    main()
