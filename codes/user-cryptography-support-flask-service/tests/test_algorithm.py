import unittest
from flask import url_for, Flask
from flask_testing import TestCase
from services.YiModifiedPaillierEncryptionPy import YiModifiedPaillierEncryptionPy
from services.PartiallyBlindSignatureClientInterface import PartiallyBlindSignatureClientInterface
import requests
import os
import json

class TestAlgorithm(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        print("\n=================")
 
      # 在結束測試時會被執行
    def tearDown(self):
        print("=================")

    def test_YiModifiedPaillierEncryptionPy(self):
        Yi = YiModifiedPaillierEncryptionPy()
        Yi.test()

    def test_PartiallyBlindSignatureClientInterface(self):
        print("測試盲簽章算法客戶端")
        url = os.environ['BANK_DJANGO_SERVICE_URL']+":8000"+"/api/login"
        result = requests.post(url, data={'account': 'user', 'password':'user'}).text
        token = json.loads(result)['token']
        user= PartiallyBlindSignatureClientInterface()
        user.generate_message_hash("Message")
        user.generate_I("Public")
        # user.step1_input(signer_step1)
        # user.generate_keypairs_parameters()