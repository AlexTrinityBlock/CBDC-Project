from app_core.models.Voucher import Voucher as VoucherModel
from app_core.services.ResolveRequest import ResolveRequest
from app_core.services.UUIDRandom import UUIDRandom
from app_core.models.User import User
from app_core.models.UserBalance import UserBalance
from django.http import HttpResponse
import json

class Voucher:
    def __init__(self):
        pass
    def generate_voucher(self,request):
        """
        用管理員帳戶生成代金券
        """
        role = ResolveRequest.ResolveRole(request)
        data = ResolveRequest.ResolvePost(request)
        # 若沒有使用者權限，則無法生成
        if role != 'administrator': 
            return HttpResponse(json.dumps({
                'code': 0,
                'message': 'User forbidden'
        }))
        token =UUIDRandom.random_uuid_string()[:10]
        voucher = VoucherModel()
        voucher.currency = data['amount']
        voucher.voucher_token = token
        voucher.save()

        return HttpResponse(json.dumps({
            'code': 1,
            'token': token
        }))

    def redeem_voucher(self,request):
        user_id = ResolveRequest.ResolveUserID(request)
        # balance = UserBalance.objects.filter(id=user_id)[0].id
        return HttpResponse(json.dumps({
            'code': 1,
        }))

