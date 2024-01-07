# model.py
# Code taken from: https://www.datacamp.com/tutorial/machine-learning-models-api-python

# Import dependencies.
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
from logger import log_this
import logging

logger = log_this(__name__, level=logging.DEBUG)
logger.info("Program started.")

# Load the dataset in a dataframe object and include only four features as mentioned
try:
    logger.info("Trying to load dataset.")
    url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
    df = pd.read_csv(url)
    include = ["Age", "Sex", "Embarked", "Survived"]  # Only four features
    df_ = df[include]
except:
    logger.error(
        "Dataset not found. Make sure you have downloaded the dataset and placed it in the correct folder."
    )

# Process the data by removing missing values and converting categorical variables to dummy variables.
try:
    categoricals = []
    for col in df_.columns:
        if (
            df_[col].dtype == "O"
        ):  # 'O' stands for 'object', indicating a categorical variable
            categoricals.append(col)
        else:
            df_[col].fillna(0, inplace=True)

    df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)

except:
    logger.error("Error while processing the dataset.")


# Modeling. Logistic Regression classifier.
try:
    dependent_variable = "Survived"
    x = df_ohe[df_ohe.columns.difference([dependent_variable])]
    y = df_ohe[dependent_variable]
    lr = LogisticRegression()
    lr.fit(x, y)
except:
    logger.error("Error while modeling.")

# Save your model
try:
    joblib.dump(lr, "model.pkl")
    logger.info("Model dumped!")
except:
    logger.error("Error while saving the model.")

# Load the model that you just saved
try:
    lr = joblib.load("model.pkl")
    logger.info("Model loaded!")
except:
    logger.error("Error while loading the model.")

# Saving the data columns from training
try:
    model_columns = list(x.columns)
    joblib.dump(model_columns, "model_columns.pkl")
    print("Models columns dumped!")
except:
    logger.error("Error while saving model columns.")
