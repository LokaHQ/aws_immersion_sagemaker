import os
from flask import Flask, Response
import sklearn
from joblib import load

app = Flask(__name__)
prefix = "/opt/ml/"
model_path = os.path.join(prefix, "model.joblib")
# model = load(model_path)

@app.route("/ping", methods=["GET"])
def ping():
    """Determine if the container is working and healthy.
    In this sample container, we declare
    it healthy if we can load the model successfully."""
    status = 200
    return Response(response="\n", status=status, mimetype="application/json")

# @app.route("/invocations", methods=["POST"])
# def predict(body):
#     pred = model.predict_proba(body)[0][0]
#     return {"pred": pred}
