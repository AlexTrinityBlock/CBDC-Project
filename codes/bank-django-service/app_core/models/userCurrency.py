from django.db import models

# 顧客的貨幣資料表
class userCurrency(models.Model):

    user_id = models.IntegerField()
    denomination =models.IntegerField()
    coin_seq= models.IntegerField()
    sign_coin_seq = models.IntegerField()
    spend_check =models.BooleanField()
    