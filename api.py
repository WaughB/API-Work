# api.py
# Code taken from: https://www.datacamp.com/tutorial/machine-learning-models-api-python

from flask import Flask, request, jsonify
import traceback
import pandas as pd
from model import lr, model_columns

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    if lr:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(lr.predict(query))

            return jsonify({"prediction": str(prediction)})

        except:
            return jsonify({"trace": traceback.format_exc()})
    else:
        print("Train the model first")
        return "No model here to use"
