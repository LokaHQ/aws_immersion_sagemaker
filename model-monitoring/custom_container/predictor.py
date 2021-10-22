import os
from flask import Flask, Response
import sklearn
from joblib import load

app = Flask(__name__)
model = load(os.environ["MODEL_PATH"])

@app.route("/ping", methods=["GET"])
def ping():
    """Determine if the container is working and healthy.
    In this sample container, we declare
    it healthy if we can load the model successfully."""
    status = 200
    return Response(response="\n", status=status, mimetype="application/json")

@app.route("/invocations", methods=["POST"])
def predict(body):
    vector = body
    pred = model.predict_proba(vector)[0][0]
    return {"pred": pred}
