from django.http import HttpResponse
import json 
from app_core.services.PartiallyBlindSignatureServerInterface import PartiallyBlindSignatureServerInterface
from app_core.services.ResolveRequest import ResolveRequest
import redis
import os

class PartiallyBlindSignature:
    def __init__(self):
        pass

    def init_blind_signature(self,request):
        token = ResolveRequest.ResolveToken(request)
        self.redis_connection = redis.Redis(host=os.environ['REDIS_IP'], port=6379, db=0, password=os.environ['REDIS_PASSWORD']) 
        status = json.loads(self.redis_connection.get(token))
        del status['BlindSignature']
        self.redis_connection.set(token,json.dumps(status))
        self.redis_connection.expire(token, 18000)
        return HttpResponse(json.dumps({
            "code": 1,
            "message": "Refresh Signature status"
        }))        

    def api_blind_signature_step_1_get_K1_Q_bit_list(self,request):
        try:
            token = ResolveRequest.ResolveToken(request)
            self.server = PartiallyBlindSignatureServerInterface(token)
            withdraw = ResolveRequest.ResolvePost(request)['withdraw']
            public_info = "withdraw:"+withdraw
            self.server.generate_I(public_info)
            result = self.server.output()
            self.server.save_and_next_step(token)
            return HttpResponse(result)
        except:
            self.init_blind_signature(request)
            return HttpResponse(json.dumps({
                "code": 0,
                "message": "Fail"
            }))        

    def api_blind_signature_step_2_get_i_list(self,request):
        try:
            token = ResolveRequest.ResolveToken(request)
            self.server = PartiallyBlindSignatureServerInterface(token)
            data = ResolveRequest.ResolvePost(request)['data']
            self.server.input(data)
            self.server.save_and_next_step(token)
            result = self.server.output()
            self.server.save_and_next_step(token)
            return HttpResponse(result)
        except:
            self.init_blind_signature(request)
            return HttpResponse(json.dumps({
                "code": 0,
                "message": "Fail"
            }))   

    def api_blind_signature_step_5_get_C(self,request):
        try:
            token = ResolveRequest.ResolveToken(request)
            self.server = PartiallyBlindSignatureServerInterface(token)
            data = ResolveRequest.ResolvePost(request)['data']
            self.server.input(data)
            self.server.save_and_next_step(token)        
            result = self.server.output()
            self.init_blind_signature(request)
            return HttpResponse(result)
        except:
            self.init_blind_signature(request)
            return HttpResponse(json.dumps({
                "code": 0,
                "message": "Fail"
            }))   