from django.db import models

# 銀行簽章過的貨幣資料表
class bankCurrency(models.Model):

    user_id = models.IntegerField()
    denomination =models.IntegerField()
    encrypt_coin_seq = models.IntegerField()
    sign_encrypt_coin_seq = models.IntegerField()
    spend_check =models.BooleanField()