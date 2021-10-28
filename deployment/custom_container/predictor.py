import numpy as np
from flask import request, Flask, Response
from joblib import load

app = Flask(__name__)
prefix = "/opt/ml/"
model_path = "sklearn_model.joblib"
model = load(model_path)

@app.route("/ping", methods=["GET"])
def ping():
    """Determine if the container is working and healthy.
    In this sample container, we declare
    it healthy if we can load the model successfully."""
    status = 200
    return Response(response="\n", status=status, mimetype="application/json")

@app.route("/invocations", methods=["POST"])
def predict():
    data = request.data.decode("utf-8")
    data = np.array([float(i) for i in data.split(",")]).reshape(1, -1)
    pred = model.predict_proba(data)[0][1]
    return {"pred": pred}
