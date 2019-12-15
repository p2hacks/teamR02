from django.db import models
#Djando.dbというモジュールにあるmodelsというパッケージに、モデル関連のクラスなどがまとめてある

class Form(models.Model):
    name = models.CharField('名前',max_length=100)
    mail = models.EmailField('mail',max_length=200)
    gender = models.BooleanField('性別')
    age = models.IntegerField('年齢',default=0)
    birthday = models.DateField('誕生日')
    egg = models.BooleanField('卵')
    shrimp = models.BooleanField('海老')
    clab = models.BooleanField('蟹')
    milk = models.BooleanField('牛乳')
    wheat = models.BooleanField('小麦')
    soba = models.BooleanField('そば')
    peanuts = models.BooleanField('落花生')
