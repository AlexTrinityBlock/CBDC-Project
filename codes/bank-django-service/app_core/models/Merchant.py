from django.db import models

# 商家的貨幣資料表
class Merchant(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    remaining = models.IntegerField()