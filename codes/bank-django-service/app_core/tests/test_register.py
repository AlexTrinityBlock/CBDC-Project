from django.test import TestCase

from app_core.models.User import User
import redis
import requests
import json
import os

class TestRegist(TestCase):
    # def test_register(self):
    #     result = requests.post('http://127.0.0.1:8000/api/register', data={'account': 'test', 'password':'test','e-mail':'test@example.com'})
    #     #result_json_object = json.loads(result.text)
    #     print(result.text)
    #     f = open("log.html", "w")
    #     f.write(result.text)
    #     f.close()
    def setUp(self):
        pass