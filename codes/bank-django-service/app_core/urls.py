from django.urls import path

from . import views

# 網址連接到View
urlpatterns = [
    # 網站頁面
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register',views.register, name = 'register'),

    # API
    path('api/login', views.api_login),
    path('api/check_login', views.api_check_login),
    path('api/logout', views.api_logout),
    path('api/register',views.api_register),

    # 密碼學 API
    path('api/blind-signature/init',views.api_blind_signature_init),
    path('api/blind-signature/get/Q',views.api_blind_signature_get_Q),
    path('api/blind-signature/get/K1',views.api_blind_signature_get_K1),
    path('api/blind-signature/step/1/get/K1/Q/bit-list',views.api_blind_signature_step_1_get_K1_Q_bit_list),
    path('api/blind-signature/step/2/get/i-list',views.api_blind_signature_step_2_get_i_list),
]

# 把不需要登入就可以瀏覽的頁面加入這裡
none_login_pages = [
    # 頁面
    "",
    "register",
    "login",
    "admin",
    # API
    "api/login",
    "api/check_login",
    "api/register",
    "api/blind-signature/get/Q",
    "api/blind-signature/get/K1",
]