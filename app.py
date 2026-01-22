from flask import Flask, render_template, request, redirect, url_for
import pickle
import mysql.connector
from feature_extraction import extract_features

app = Flask(__name__)

# Load model
model = pickle.load(open("model/phishing_model.pkl", "rb"))

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tousif@953862",
    database="phishing_db"
)
cursor = db.cursor()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        features = extract_features(url)

        # Probability-based prediction
        phishing_prob = model.predict_proba([features])[0][1]

        if phishing_prob > 0.65:
            result = "phishing"
        else:
            result = "safe"

        cursor.execute(
            "INSERT INTO url_logs (url, result) VALUES (%s, %s)",
            (url, result)
        )
        db.commit()

        return redirect(url_for("result", status=result))

    return render_template("index.html")


@app.route("/result")
def result():
    status = request.args.get("status")
    return render_template("result.html", status=status)

 import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


