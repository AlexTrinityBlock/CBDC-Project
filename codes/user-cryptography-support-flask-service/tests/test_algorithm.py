import unittest
from flask import url_for, Flask
from flask_testing import TestCase
from services.YiModifiedPaillierEncryptionPy import YiModifiedPaillierEncryptionPy
from services.PartiallyBlindSignatureClientInterface import PartiallyBlindSignatureClientInterface

class TestAlgorithm(TestCase):
    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        print("set up")
 
      # 在結束測試時會被執行
    def tearDown(self):
        print("tear down")

    def test_YiModifiedPaillierEncryptionPy(self):
        Yi = YiModifiedPaillierEncryptionPy()
        Yi.test()

    def test_PartiallyBlindSignatureClientInterface(self):
        user= PartiallyBlindSignatureClientInterface()
        user.generate_message_hash("Message")
        user.generate_I("Public")
        # user.step1_input(signer_step1)
        user.generate_keypairs_parameters()