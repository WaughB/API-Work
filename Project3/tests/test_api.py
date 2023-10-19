#####################
##### Libraries #####
#####################

from flask_testing import TestCase
from api import app, lr, model_columns

##########################
##### Test base case #####
##########################

class ApiBaseTest(TestCase):

    def create_app(self):
        return app

    ######################
    ##### Prediction #####
    ######################

    def test_prediction(self):
            sample_payload = [
                {"Age": 30, "Sex": "male", "Embarked": "S"},
                {"Age": 25, "Sex": "female", "Embarked": "C"}
            ]
            response = self.client.post('/predict', json=sample_payload)
            self.assertEqual(response.status_code, 200)
            self.assertIn("prediction", response.json)


    ############################
    ##### Input validation #####
    ############################

    def test_invalid_payload_missing_fields(self):
        invalid_payload = [{"Age": 30, "Sex": "male"}]
        response = self.client.post('/predict', json=invalid_payload)
        self.assertEqual(response.status_code, 400)

    def test_invalid_payload_wrong_datatype(self):
        invalid_payload = [{"Age": "thirty", "Sex": "male", "Embarked": "S"}]
        response = self.client.post('/predict', json=invalid_payload)
        self.assertEqual(response.status_code, 400)

    #################################
    ##### Endpoint Availability #####
    #################################

    def test_endpoint_availability(self):
        response = self.client.get('/predict')
        self.assertNotEqual(response.status_code, 404)

    ######################
    ##### Edge cases #####
    ######################

    def test_null_payload(self):
        response = self.client.post('/predict', json=None)
        self.assertEqual(response.status_code, 400)


#########################
##### Model loading #####
#########################

def test_model_loading():
    from api import lr, model_columns
    assert lr is not None, "Model not loaded"
    assert model_columns is not None, "Model columns not loaded"