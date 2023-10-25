#####################
##### Libraries #####
#####################

import os
import requests
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Constants
DATA_URL = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
TEST_DATA_PATH = "test_data.csv"
MODEL_PATH = "test_model.pkl"
MODEL_COLUMNS_PATH = "test_model_columns.pkl"

#################
##### Setup #####
#################

def setup_test_data():
    data = pd.read_csv(DATA_URL)
    test_data = data.sample(frac=0.1)
    test_data.to_csv(TEST_DATA_PATH, index=False)
    return test_data

##########################
##### Load the data ######
##########################

def load_data():
    return pd.read_csv(TEST_DATA_PATH)

###############################
##### Preprocess the data #####
###############################

def preprocess_data(data):
    data['Age'].fillna(data['Age'].mean(), inplace=True)
    data = pd.get_dummies(data, columns=['Sex', 'Embarked'])
    return data

###########################
##### Train the model #####
###########################

def train_model(data):
    X = data[['Age', 'Sex_female', 'Sex_male', 'Embarked_C', 'Embarked_Q', 'Embarked_S']]
    y = data['Survived']
    model = LogisticRegression(max_iter=500)
    model.fit(X, y)
    return model, X.columns.tolist()

###############################
##### Test: Load the data #####
###############################

def test_load_data():
    setup_test_data()
    data = load_data()
    assert 'Age' in data.columns
    assert 'Sex' in data.columns
    assert 'Embarked' in data.columns

#####################################
##### Test: Preprocess the data #####
#####################################

def test_preprocess_data():
    data = load_data()
    processed_data = preprocess_data(data)
    assert not processed_data['Age'].isnull().any()
    assert 'Sex_male' in processed_data.columns
    assert 'Sex_female' in processed_data.columns
    assert 'Embarked_C' in processed_data.columns
    assert 'Embarked_Q' in processed_data.columns
    assert 'Embarked_S' in processed_data.columns

#################################
##### Test: Train the model #####
#################################

def test_train_model():
    data = load_data()
    processed_data = preprocess_data(data)
    model, _ = train_model(processed_data)
    assert model

####################################
##### Test: Evaluate the model #####
####################################

def test_evaluate_model():
    data = load_data()
    processed_data = preprocess_data(data)
    X = processed_data[['Age', 'Sex_female', 'Sex_male', 'Embarked_C', 'Embarked_Q', 'Embarked_S']]
    y = processed_data['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LogisticRegression(max_iter=500)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    assert accuracy > 0.5  # assuming a basic threshold for model validity

###############################
##### Test: Model columns #####
###############################

def test_model_columns():
    data = load_data()
    processed_data = preprocess_data(data)
    _, columns = train_model(processed_data)
    expected_columns = ['Age', 'Sex_female', 'Sex_male', 'Embarked_C', 'Embarked_Q', 'Embarked_S']
    assert columns == expected_columns

##################################
##### Test: Model prediction #####
##################################

def test_model_prediction():
    data = load_data()
    processed_data = preprocess_data(data)
    model, _ = train_model(processed_data)
    sample_data = {
        'Age': 25,
        'Sex_female': 1,
        'Sex_male': 0,
        'Embarked_C': 0,
        'Embarked_Q': 0,
        'Embarked_S': 1
    }
    prediction = model.predict([list(sample_data.values())])[0]
    assert prediction in [0, 1]
