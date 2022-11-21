# docker-compose exec user-cryptography-support-flask-service bash
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
        
        # 取得token
        url = os.environ['BANK_DJANGO_SERVICE_URL']
        result = requests.post(url+"/api/login", data={'account': 'user', 'password':'user'}).text
        token = json.loads(result)['token']

        print(token)

        signer_step1 = requests.post(url+"/api/blind-signature/step/1/get/K1/Q/bit-list", data={'token': token}).text

        print(signer_step1)

        user= PartiallyBlindSignatureClientInterface()
        user.generate_message_hash("Message")
        user.generate_I("Public")
        user.step1_input(signer_step1)
        user.generate_keypairs_parameters()
        user_step1 = user.step1_output()

        signer_step2 = requests.post(url+"/api/blind-signature/step/2/get/i-list", data={'token': token, 'data':user_step1}).text
        print(signer_step2)

        user.step3_input(signer_step2)
        user_step4 = user.step4_output()
        print(user_step4)

        requests.post(url+"/api/logout", data={'token': token})
        # text = requests.post(url+"/api/blind-signature/init", data={'token': token}).text
        
        
