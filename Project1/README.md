# Project description
This project is inspired by a [DataCamp tutorial](https://www.datacamp.com/tutorial/machine-learning-models-api-python) that I was recently looking at. The heart of the code comes from the tutorial.

The program itself is made to expose a machine learning model API. The original dataset is the famous [Titanic dataset](https://www.kaggle.com/competitions/titanic). The backend relies on Flask to serve the API. This is a no frills version of this project. 

# How to run
To execute the program run:
`python model.py`

 Then afterwards run:
`python api.py`

# Sample output
If all goes well, you should see four files in the directory after running:
* model.py
* api.py
* model.pkl
* model_columns.pkl

After this you will be able to access the API. For this example I used [Postman](https://www.postman.com/) and sent this information: 

[
    {"Age": 85, "Sex": "male", "Embarked": "S"},
    {"Age": 24, "Sex": "female", "Embarked": "C"}
]

This is what it returned to me: [](/images/Postman-working.png)