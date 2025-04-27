from flask import Flask, render_template, request

app = Flask(__name__)

def predict_risk(age, bmi, systolic_bp, diastolic_bp, cholesterol, glucose):
    risk_score = (
        0.2 * age +
        0.3 * bmi +
        0.1 * systolic_bp +
        0.1 * diastolic_bp +
        0.2 * cholesterol / 3 +
        0.1 * glucose / 5
    )
    risk_score = min(10, max(1, risk_score / 10))
    return round(risk_score, 2)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        age = float(request.form["age"])
        bmi = float(request.form["bmi"])
        systolic_bp = float(request.form["systolic_bp"])
        diastolic_bp = float(request.form["diastolic_bp"])
        cholesterol = float(request.form["cholesterol"])
        glucose = float(request.form["glucose"])

        risk = predict_risk(age, bmi, systolic_bp, diastolic_bp, cholesterol, glucose)
        return render_template("result.html", risk=risk)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
