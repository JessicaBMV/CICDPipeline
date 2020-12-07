from locust import HttpUser, task, TaskSet
import json

class MyUser(HttpUser):
    wait_time = constant(1)
    host = 'https://jess-pipeline.azurewebsites.net'

    @task
    def home(self):
        response = self.client.get("/")
        print("Response status code:", response.status_code)
        print("Response text:", response.text)

    @task
    def predict(self):
        headers = {'content-type': 'application/json'}
        payload = {
            "CHAS":{
            "0":0
            },
            "RM":{
            "0":6.575
            },
            "TAX":{
            "0":296.0
            },
            "PTRATIO":{
            "0":15.3
            },
            "B":{
            "0":396.9
            },
            "LSTAT":{
            "0":4.98
            }
        }
        response = self.client.post("/predict", data=json.dumps(payload), headers=headers)
        print("Response status code:", response.status_code)
        print("Response text:", response.text)


        