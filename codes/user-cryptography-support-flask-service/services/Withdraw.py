import unittest
from flask import url_for, Flask
from flask_testing import TestCase
from services.YiModifiedPaillierEncryptionPy import YiModifiedPaillierEncryptionPy
from services.PartiallyBlindSignatureClientInterface import PartiallyBlindSignatureClientInterface
import requests
import os
import json

class Withdraw:
    def __init__(self):
        pass
    def withdraw(self,request):
        print("測試盲簽章算法客戶端")

        # 取得token
        url = os.environ['BANK_DJANGO_SERVICE_URL']
        result = requests.post(url+"/api/login", data={'account': 'user', 'password':'user'}, timeout=3).text
        token = json.loads(result)['token']

        signer_step1 = requests.post(url+"/api/blind-signature/step/1/get/K1/Q/bit-list", data={'token': token,'withdraw':1}, timeout=3).text
        signer_step1 = json.loads(signer_step1)

        user= PartiallyBlindSignatureClientInterface()
        user.generate_message_hash("Message")
        user.generate_I(signer_step1['PublicInfomation'])
        print("I:",user.I)
        user.step1_input(signer_step1)
        user.generate_keypairs_parameters()
        user_step1 = user.step1_output()

        signer_step2 = requests.post(url+"/api/blind-signature/step/2/get/i-list", data={'token': token, 'data':user_step1}, timeout=3).text

        user.step3_input(signer_step2)
        user_step4 = user.step4_output()
        
        signer_step5 = requests.post(url+"/api/blind-signature/step/5/get/C", data={'token': token, 'data':user_step4}, timeout=3).text

        return signer_step5