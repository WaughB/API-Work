# main.py
from flask import Flask, request, jsonify
import joblib
from api import app
import sys
from logger import log_this
import logging
from api import app

if __name__ == "__main__":
    # Initialize the logger. If no log file is specified, logs will just save to .
    # Other logging levels are logging.DEBUG, logging.WARNING, logging.ERROR, logging.CRITICAL.
    logger = log_this(__name__, level=logging.DEBUG)
    logger.info("Program started.")

    # Assign port number.
    try:
        logger.info("Trying to get port from command line.")
        port = int(sys.argv[1])  # This is for a command-line input
    except:
        logger.info("No port provided. Using default port 12345.")
        port = 12345  # If you don't provide any port the port will be set to 12345

    # Assign model file names.
    try:
        logger.info("Trying to get model file name from command line.")
        model_file_name = sys.argv[2]  # This is for a command-line input
    except:
        logger.info("No model file name provided. Using default model.pkl.")
        model_file_name = "model.pkl"

    # Assign model columns file names.
    try:
        logger.info("Trying to get model columns file name from command line.")
        model_columns_file_name = sys.argv[3]  # This is for a command-line input

    except:
        logger.info(
            "No model columns file name provided. Using default model_columns.pkl."
        )
        model_columns_file_name = "model_columns.pkl"

    # Load the model and model columns.
    try:
        logger.info("Trying to load model.")
        lr = joblib.load(model_file_name)  # Load "model.pkl"
        logger.info(f"Loaded model from {model_file_name}.")
    except:
        logger.info("Model not found. Exiting.")
        exit()

    app.run(port=port, debug=True)
