# Code taken from: https://www.datacamp.com/tutorial/machine-learning-models-api-python

#####################
##### Libraries #####
#####################

from flask import Flask, request, jsonify
import joblib
import traceback
import pandas as pd
import numpy as np
import pickle

##########################
##### Define the API #####
##########################

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if not lr:
        return jsonify({'error': 'Model not loaded'}), 500

    # Check for the correct content type
    if request.content_type != 'application/json':
        return jsonify({'error': 'Expected content type: application/json'}), 400

    json_ = request.json

    # Check for null payload
    if json_ is None:
        return jsonify({'error': 'Payload is null'}), 400

    # Check for required fields
    required_fields = ['Age', 'Sex', 'Embarked']
    for record in json_:
        missing_fields = [field for field in required_fields if field not in record]
        if missing_fields:
            return jsonify({'error': f'Missing fields: {", ".join(missing_fields)}'}), 400

        # Clean and validate data
        record['Sex'] = record['Sex'].lower()  # Convert Sex to lowercase
        record['Embarked'] = record['Embarked'].upper()  # Convert Embarked to uppercase

        if not isinstance(record['Age'], (int, float)):
            return jsonify({'error': 'Age should be a number'}), 400

        if record['Sex'] not in ['male', 'female']:
            return jsonify({'error': 'Invalid value for Sex'}), 400

        if record['Embarked'] not in ['S', 'C', 'Q']:
            return jsonify({'error': 'Invalid value for Embarked'}), 400

    # Convert to dataframe and make predictions
    query = pd.get_dummies(pd.DataFrame(json_))
    query = query.reindex(columns=model_columns, fill_value=0)
    prediction = list(lr.predict(query))

    return jsonify({'prediction': str(prediction)}), 200

################
##### Main #####
################

lr = joblib.load("model.pkl") # Load "model.pkl"
print('Model loaded')
model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
print('Model columns loaded')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    app.run(host='0.0.0.0', port=port, debug=True)