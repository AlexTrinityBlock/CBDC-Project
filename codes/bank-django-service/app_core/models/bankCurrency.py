from django.db import models

# 銀行簽章過的貨幣資料表
class bankCurrency(models.Model):

    user_id = models.CharField(default="user_id",max_length=100)
    denomination =models.IntegerField(default=0)
    encrypt_coin_seq = models.CharField(default="encrypt_coin_seq",max_length=100)
    sign_encrypt_coin_seq = models.CharField(default="sign_encrypt_coin_seq",max_length=100)
    spend_check =models.BooleanField(default=False)