from django.urls import path

from . import views

# 網址連接到View
urlpatterns = [
    # 網站頁面
    path('', views.index, name='index'),
    path('login', views.login, name='login'),

    # API
    path('api/login', views.api_login),
    path('api/check_login', views.api_check_login),
    path('api/logout', views.api_logout),
]

# 把不需要登入就可以瀏覽的頁面加入這裡
none_login_pages = [
    "login",
    "admin",
    "api/login",
    "api/check_login",
]