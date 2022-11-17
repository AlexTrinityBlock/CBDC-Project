from django.test import TestCase
import os
import json
from pprint import pprint
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey, PublicKey
from app_core.services.YiModifiedPaillierEncryptionPy import YiModifiedPaillierEncryptionPy
from app_core.services.PartiallyBlindSignatureClientInterface import PartiallyBlindSignatureClientInterface
from app_core.services.PartiallyBlindSignatureServerInterface import PartiallyBlindSignatureServerInterface
from app_core.services.Login import Login
import requests
import redis

class TestAlgorithm(TestCase):
    
    def setUp(self):
        self.ECDSA_PUBLICKEY = os.environ['ECDSA_PUBLICKEY']
        self.ECDSA_PRIVATEKEY = os.environ['ECDSA_PRIVATEKEY']
        pass

    # 測試Yi算法
    def test_YiModifiedPaillierEncryptionPy(self):
        print("[算法測試] 測試Yi同態加密")
        yiModifiedPaillierEncryptionPy = YiModifiedPaillierEncryptionPy()
        yiModifiedPaillierEncryptionPy.test()

    # 測試ECDSA模塊
    def test_ECDSA(self):
        print("[算法測試] ECDSA模塊")
        privateKey = PrivateKey.fromPem(self.ECDSA_PRIVATEKEY)
        publicKey = PublicKey.fromPem(self.ECDSA_PUBLICKEY)
        message = json.dumps({"data": "123"})
        signature = Ecdsa.sign(message, privateKey)
        result = Ecdsa.verify(message, signature, publicKey)
        self.assertTrue(result, "\n\n ECDSA模塊測試失敗，有可能是模塊損壞或者ECDSA鑰匙錯誤")

    def test_PartiallyBlindSignatureServerInterface(self):
        redis_connection_0 = redis.Redis(host=os.environ['REDIS_IP'], port=6379, db=0, password=os.environ['REDIS_PASSWORD']) 
        redis_connection_1 = redis.Redis(host=os.environ['REDIS_IP'], port=6379, db=1, password=os.environ['REDIS_PASSWORD']) 

        login = Login()
        token = login.setUserToken("user")

        signer = PartiallyBlindSignatureServerInterface(token)
        signer_step1 = signer.output()
        signer.save_and_next_step(token)

        user = PartiallyBlindSignatureClientInterface()
        user.generate_message_hash("Message")
        user.generate_I("Public")
        user.step1_input(signer_step1)
        user.generate_keypairs_parameters()
        user_step1 = user.step1_output()

        signer.input(user_step1)
        signer.save_and_next_step(token)
        signer_step3 = signer.output()
        signer.save_and_next_step(token)
        
        user.step3_input(signer_step3)
        use_step4_output = user.step4_output()

        signer.input(use_step4_output)
        signer.save_and_next_step(token)

        signer_step5 = signer.output()
        user.step5_input(signer_step5)

        # 檢查 C1, C2
        Yi = YiModifiedPaillierEncryptionPy()
        signer_C1 = signer.status["C1"]
        signer_C2 = signer.status["C2"]
        user_C1 = user.C1
        user_C2 = user.C2
        # result1 = Yi.decrypt(user_C1,user.p,user.k,user.q,user.N)
        # print("原始C1: ",user.message_hash)
        # print("解密後C1: ",result1)
        # print("\n\n")
        # result2 = Yi.decrypt(user_C2,user.p,user.k,user.q,user.N)
        # print("原始C2: ",user.t)
        # print("解密後C2: ",result2)
        # print("C2^d: ",signer.C2_mul_d_mod_q)

        redis_connection_0.delete(token)
        redis_connection_1.delete('user')