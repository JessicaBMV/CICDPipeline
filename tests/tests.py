import sys
from pathlib import Path
import unittest
sys.path.append(str(Path('.').absolute().parent))
from app import create_app
from flask import Flask
import json


class TestPurchaseRequest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_client = self.app.test_client()

    def test_home(self):
        print(self.app_client)
        response =  self.app_client.get("/")
        self.assertEqual(response.status_code, 200)
        

    def test_predict(self):
        
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        data = {
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
        response = self.app_client.post('/predict',
                                 data=json.dumps(data),
                                 content_type='application/json',  headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)
        self.assertEqual(response.data , b'{"prediction":[20.35373177134412]}\n')
