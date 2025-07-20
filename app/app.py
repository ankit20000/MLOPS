from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model/model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = np.array(request.json["input"]).reshape(1, -1)
    prediction = model.predict(data).tolist()
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
