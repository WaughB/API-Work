# test_api.py
import json
import pytest
from api import app  # Import the Flask application
from unittest.mock import patch


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_predict_valid_input(client):
    # Valid input data
    data = [
        {"Age": 30, "Sex": "male", "Embarked": "S"},
        {"Age": 25, "Sex": "female", "Embarked": "C"},
    ]

    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "prediction" in response.json


def test_predict_missing_field(client):
    # Missing field in input data
    data = [{"Age": 30, "Sex": "male"}, {"Age": 25, "Embarked": "C"}]

    response = client.post("/predict", json=data)
    assert response.status_code == 200  # Expecting a successful response


def test_predict_empty_input(client):
    response = client.post("/predict", json=[])
    assert response.status_code != 200
    assert "trace" in response.json


def test_predict_no_model(client):
    with patch("api.lr", None):  # Adjust the path as necessary
        data = [
            {"Age": 85, "Sex": "male", "Embarked": "S"},
            {"Age": 24, "Sex": "female", "Embarked": "C"},
        ]
        response = client.post("/predict", json=data)
        assert response.status_code != 200  # Expecting an error status code


def test_predict_success(client):
    valid_data = [
        {"Age": 30, "Sex": "male", "Embarked": "S"},
        {"Age": 24, "Sex": "female", "Embarked": "C"},
    ]

    response = client.post("/predict", json=valid_data)
    assert response.status_code == 200
    assert "prediction" in response.json
