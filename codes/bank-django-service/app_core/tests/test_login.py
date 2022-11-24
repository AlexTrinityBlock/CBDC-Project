from django.test import TestCase
from app_core.services.Login import Login
from app_core.models.User import User
from django.test.client import RequestFactory
import redis
import requests
import json
import os


class TestLogin(TestCase):
    """測試登入系統
    確認登入系統是否正常
    """
    # 測試初始設置
    def setUp(self):
        # 網址路徑
        self.login_url = 'http://localhost:8000/api/login'
        self.check_login_url = 'http://localhost:8000/api/check_login'
        # 使用者帳號與密碼的Hash
        self.account = "user"
        self.password = 'user'
        self.password_hash = "04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb"
        # 建立測試用使用者資料
        User.objects.create(account = self.account)
        User.objects.create(password_hash = self.password_hash)
        # 建立 Redis 連線
        self.redis_connection_token_index = redis.Redis(host=os.environ['REDIS_IP'], port=6379, db=0, password=os.environ['REDIS_PASSWORD'])
        self.redis_connection_user_index = redis.Redis(host=os.environ['REDIS_IP'], port=6379, db=1, password=os.environ['REDIS_PASSWORD'])
        
    # 測試登入
    def test_Login(self):
        login = Login()
        # 正確登入
        print("[登入測試] 正確登入測試")
        result = requests.post(self.login_url, data={'account': self.account, 'password':self.password})
        result_json_object = json.loads(result.text)
        self.assertEqual(result_json_object['code'], 1, '\n\n正確登入測試失敗!')

        # user = User()
        # user.account = 'user1'
        # user.password_hash = '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb'
        # user.e_mail = '1235456464'
        # user.save()
        # rf = RequestFactory()
        # post_request = rf.post('/api/login/', {'account': 'user1', 'password':'user'})
        # # login = Login()
        # response = login.login(post_request)
        # print(response)
        # result = json.loads(response.content.decode("utf-8"))
        # self.assertEqual(result['code'], 1, '\n\n正確登入測試失敗!')

        print("[登入測試] 檢查Redis是否正確存有Token")
        token = self.redis_connection_user_index.get(self.account).decode('utf-8')
        asserted_token = result_json_object['token']
        self.assertEqual(token, asserted_token)

        print("[登入測試] 測試登入檢查器")
        result_check_login = requests.get(self.check_login_url, params={'token': token})
        result_json_object_2 = json.loads(result_check_login.text)
        self.assertEqual(result_json_object_2['code'], 1)
        
        print("[登入測試] 刪除Token")
        self.redis_connection_token_index.delete(token)
        self.redis_connection_user_index.delete(self.account)
        
        # 錯誤登入
        print("[登入測試] 登入失敗判別測試")
        result = requests.get(self.login_url, params={'account': self.account, 'password':'wrong password'})
        result_json_object = json.loads(result.text)
        self.assertEqual(result_json_object['code'], 0)
        # self.assertTrue(False)
        # self.assertFalse(False)