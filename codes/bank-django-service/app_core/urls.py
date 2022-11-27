from django.urls import path

from . import views

# 網址連接到View
urlpatterns = [
    # 網站頁面
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register',views.register, name = 'register'),

    # 使用者登入API
    path('api/login', views.api_login),
    path('api/check_login', views.api_check_login),
    path('api/logout', views.api_logout),
    path('api/register',views.api_register),

    # 密碼學 API
    path('api/blind-signature/init',views.api_blind_signature_init),
    path('api/blind-signature/get/Q',views.api_blind_signature_get_Q),
    path('api/blind-signature/get/K1',views.api_blind_signature_get_K1),
    path('api/blind-signature/get/q',views.api_blind_signature_get_q),
    path('api/blind-signature/step/1/get/K1/Q/bit-list',views.api_blind_signature_step_1_get_K1_Q_bit_list),
    path('api/blind-signature/step/2/get/i-list',views.api_blind_signature_step_2_get_i_list),
    path('api/blind-signature/step/5/get/C',views.api_blind_signature_step_5_get_C),

    # 管理員專用API
    path('api/administrator/login', views.api_administrator_login),
    path('api/administrator/check_login', views.api_administrator_check_login),
    path('api/administrator/logout', views.api_administrator_logout),

    # 生成代金券序號
    path('api/generate/voucher', views.api_generate_voucher),
    path('api/redeem/voucher', views.redeem_voucher),

    # 使用者兌換貨幣
    path('api/redeem/currency', views.redeem_currency),
    path('api/get/balance', views.get_balance),
    path('api/get/user_payment_id', views.bank_user_payment_id),

    # 使用者 AES　功能，設置 AES 認證密文
    path('api/set/aes-verify-ciphertext', views.api_set_aes_verify_ciphertext),
    path('api/get/aes-verify-ciphertext', views.api_get_aes_verify_ciphertext),

]

# 把不需要登入就可以瀏覽的頁面加入這裡
none_login_pages = [
    # 頁面
    "",
    "register",
    "login",
    # API
    "api/login",
    "api/check_login",
    "api/register",
    "api/blind-signature/get/Q",
    "api/blind-signature/get/K1",
    "api/blind-signature/get/q",
    "api/administrator/login",
    "api/administrator/check_login",
    "api/administrator/logout",
    "api/administrator/check_login",
    "api/administrator/logout",
    "api/redeem/currency",
]