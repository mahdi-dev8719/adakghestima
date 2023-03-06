from django.db import models
from django.conf import settings


class Price(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current = models.IntegerField('قیمت حال',default=0)
    prod = models.IntegerField('قیمت محصول',default=0)
    compare = models.IntegerField('قیمت مقایسه شده',default=0)
    difference = models.IntegerField('قیمت تفاضل ',default=0)
    car = models.IntegerField('قیمت ماشین',default=0)

    class Meta:
        verbose_name = 'قیمت'
        verbose_name_plural = 'قیمت ها'


class Car(models.Model):
    car_price = models.IntegerField('قیمت',default=0)
    new = models.IntegerField('قیمت',default=0)
    affrodable = models.IntegerField('قیمت',default=0)

    class Meta:
        verbose_name = 'قیمت ماشین'
        verbose_name_plural = 'قیمت ماشین ها'