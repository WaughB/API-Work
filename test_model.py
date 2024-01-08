import pytest
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from model import (
    lr,
    model_columns,
)


def test_data_loading():
    url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
    df = pd.read_csv(url)
    assert not df.empty, "Dataframe should not be empty after loading data"


def test_preprocessing():
    include = ["Age", "Sex", "Embarked", "Survived"]
    df = pd.read_csv(
        "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
    )
    df_ = df[include]
    df_["Age"].fillna(0, inplace=True)  # Example preprocessing step
    assert (
        df_["Age"].isnull().sum() == 0
    ), "No null values should be in Age column after preprocessing"


def test_model_training():
    df = pd.read_csv(
        "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
    )
    df_ = df[["Age", "Sex", "Embarked", "Survived"]]

    # Fill NaN values in all columns to handle both categorical and numerical columns
    df_.fillna({"Age": 0, "Sex": "unknown", "Embarked": "unknown"}, inplace=True)

    df_ohe = pd.get_dummies(df_, columns=["Sex", "Embarked"], dummy_na=False)
    x = df_ohe[df_ohe.columns.difference(["Survived"])]
    y = df_ohe["Survived"]

    model = LogisticRegression()
    model.fit(x, y)
    assert model, "Model should be trained"


def test_model_saving_loading():
    model = LogisticRegression()
    joblib.dump(model, "test_model.pkl")
    loaded_model = joblib.load("test_model.pkl")
    assert loaded_model, "Model should be loaded successfully"


def test_model_columns_saving():
    columns = ["col1", "col2", "col3"]  # Example columns
    joblib.dump(columns, "test_model_columns.pkl")
    loaded_columns = joblib.load("test_model_columns.pkl")
    assert loaded_columns == columns, "Model columns should be loaded successfully"
