from app_core.services.ResolveRequest import ResolveRequest
from app_core.models.UsedCurrency import UsedCurrency
from app_core.models.UserBalance import UserBalance
from app_core.models.User import User
from django.http import HttpResponse
import json
import os
import requests

class RedeemCurrency:
    def __init__(self):
        pass

    def redeem_currency(self, request):
        # 取得輸入資料
        data = ResolveRequest.ResolvePost(request)
        message = data["message"]
        Info = data["Info"]
        R = data["R"]
        s = data["s"]
        t = data["t"]
        bank_user_payment_id = data["bank_user_payment_id"]

        # 檢查貨幣是否被使用過
        is_used = UsedCurrency.objects.filter(message=message,Info=Info,R=R,s=s,t=t).count()
        if is_used > 0:
            return HttpResponse(json.dumps({
                'code':0,
                'message':'Signature is used'
            }))

        # 傳送檢查請求到檢查數位貨幣的服務
        url = os.environ["USER_CRYPTOGRAPHY_SUPPORT_FLASK_SERVICE_URL"] + '/verify/currency'
        result = requests.post(url, data={'message':message,'Info':Info,'R': R, 's':s, 't':t}).text
        result = json.loads(result)
        if result['code'] == 0: #若驗證失敗
            return HttpResponse(json.dumps({
                'code':0,
                'message':'Invalid signature.'
            }))

        # 取得貨幣額度
        amount = json.loads(Info)['currency']

        # 將額度存入使用者帳戶
        id = User.objects.filter(bank_user_payment_id=bank_user_payment_id)[0].id
        user_balance = UserBalance.objects.filter(user_id=id)[0]
        user_balance.balance = user_balance.balance + int(amount)
        user_balance.save()

        # 將使用過的盲簽章進行儲存
        used_currency = UsedCurrency()
        used_currency.message = message
        used_currency.Info = Info
        used_currency.R = R
        used_currency.s = s
        used_currency.t = t
        used_currency.save()

        return HttpResponse(json.dumps({
            'code':1,
            'message':'Successful transaction.'
        }))
