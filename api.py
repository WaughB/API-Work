# api.py

from flask import Flask, request, jsonify
import traceback
import pandas as pd
from model import lr, model_columns
from logger import log_this
import logging

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    logger = log_this(__name__, level=logging.DEBUG)
    logger.info("Program started.")
    if lr is None:
        logger.error("Model not loaded.")
        return jsonify({"error": "Model not loaded."}), 500  # Return a 500 error code

    try:
        json_ = request.json
        query_df = pd.DataFrame(json_)

        # Check for missing columns and add them as needed
        logger.debug(f"Model columns: {model_columns}")
        missing_cols = set(model_columns) - set(query_df.columns)
        for c in missing_cols:
            query_df[c] = 0

        # Ensure the order of columns matches that of the training data
        logger.debug(f"Query columns: {query_df.columns}")
        query_df = query_df[model_columns]

        # Convert categorical variables to dummy variables
        logger.debug(f"Query df: {query_df}")
        query = pd.get_dummies(query_df)

        # Fill missing dummy variables
        logger.debug(f"Query df after get_dummies: {query}")
        missing_dummies = set(model_columns) - set(query.columns)
        for d in missing_dummies:
            query[d] = 0

        prediction = list(lr.predict(query))
        logger.info(f"Prediction: {prediction}")

        return jsonify({"prediction": str(prediction)})

    except Exception as e:
        logger.error(f"Error during prediction: {traceback.format_exc()}")
        return jsonify({"trace": traceback.format_exc()}), 500


if __name__ == "__main__":
    app.run(debug=True)
