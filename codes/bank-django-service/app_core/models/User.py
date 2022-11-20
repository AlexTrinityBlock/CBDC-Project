from django.db import models

# 使用者資料表
class User(models.Model):
    """使用者資料表
    未完成
    撰寫: 蕭維均
    """
    account = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_num = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    e_mail = models.CharField(null=True,max_length= 100)
    phone = models.CharField(max_length=100)
    remaining = models.CharField(max_length=100)

    