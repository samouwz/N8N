from flask import Flask, request, jsonify
import random
import datetime

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    match = data.get("match")

    outcomes = [
        ("Home Win", 0.65),
        ("Draw", 0.20),
        ("Away Win", 0.15)
    ]

    prediction = random.choice(outcomes)

    log = {
        "match": match,
        "prediction": prediction[0],
        "confidence": prediction[1],
        "time": str(datetime.datetime.now())
    }

    print(log)  # simple telemetry/logging

    return jsonify(log)

if __name__ == "__main__":
    app.run(debug=True)

