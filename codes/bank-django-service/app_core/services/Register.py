from django.http import HttpResponse
from app_core.models.User import User
import hashlib

import json 

class Register():
    def register(self,request):
            # 無論GET或者POST都接收，之後依照需求修改
        if request.method == 'GET':
            result = {'code':0, 'message':'Registe post required'}
            result = json.dumps(result)
            return HttpResponse(result)
        elif request.method == 'POST':
            # 適應不同的Fetch POST 實現
            try:
                data = json.loads(request.body)
            except:
                data = request.POST
        # print(data['account'])
        password = data['password']
        password = password.encode('utf-8')
        password_hash = hashlib.sha256(password).hexdigest()
        user = User()
        user_account_number = User.objects.filter(account__contains=data['account']).count() #數帳號
        if(user_account_number>0): 
            result = {'code':2, 'message':'account is created'}
            result = json.dumps(result)
            return HttpResponse(result)

        user.account = data['account']
        user.e_mail = data['e_mail']
        user.password_hash = password_hash
        user.save()
        result = {'code':1, 'message':'registe success.'}
        result = json.dumps(result)
        return HttpResponse(result)