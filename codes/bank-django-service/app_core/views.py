from django.shortcuts import render
from django.http import HttpResponse
from app_core.services.Login import Login
from app_core.services.Register import Register
from app_core.services.PartiallyBlindSignaturePublicParameters import PartiallyBlindSignaturePublicParameters
from app_core.services.PartiallyBlindSignature import PartiallyBlindSignature
"""
前端頁面

請先在templates資料夾中建立HTML
然後依照以下方式建立一個連接到頁面的view:

def 頁面名稱(request):
    return render(request, '頁面名稱/index.html')

之後到 urls.py 來將網址聯繫到這個view
"""
def index(request):
    return render(request, 'index/index.html')

def home(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'login/index.html')

def register(request):
    return render(request, 'register/index.html')

"""
API

使用方法如下:

def 此API的名稱(request):
    自己建立的model實例 = 自己建立的model()
    回傳結果 = 自己建立的model實例.方法(request)
    return HttpResponse(回傳結果)

之後到 urls.py 來將網址聯繫到這個view
"""
def api_login(request):
    login =Login()
    return login.login(request)

def api_logout(request):
    login =Login()
    return login.logout(request)

# 檢查登入 API
def api_check_login(request):
    login =Login()
    return login.check_login(request)

def api_register(request):
    register =Register()
    return register.register(request)

"""
密碼學 API
"""
def api_blind_signature_init(request):
    obj = PartiallyBlindSignature()
    return obj.init_blind_signature(request)

def api_blind_signature_get_Q(request):
    obj = PartiallyBlindSignaturePublicParameters()
    return obj.get_Q()

def api_blind_signature_get_K1(request):
    obj = PartiallyBlindSignaturePublicParameters()
    return obj.get_K1()

def api_blind_signature_get_q(request):
    obj =PartiallyBlindSignaturePublicParameters()
    return obj.get_q()

def api_blind_signature_step_1_get_K1_Q_bit_list(request):
    obj = PartiallyBlindSignature()
    return obj.api_blind_signature_step_1_get_K1_Q_bit_list(request)

def api_blind_signature_step_2_get_i_list(request):
    obj = PartiallyBlindSignature()
    return obj.api_blind_signature_step_2_get_i_list(request)

def api_blind_signature_step_5_get_C(request):
    obj = PartiallyBlindSignature()
    return obj.api_blind_signature_step_5_get_C(request)