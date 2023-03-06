from django.db import models
from django.conf import settings

class Profile(models.Model):

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="Profiles")

    username = models.CharField("نام کاربری", max_length=20 )
    phone_number = models.IntegerField("شماره موبایل" , default=0)
    email = models.EmailField("ایمیل" )

    my_ads = models.CharField( "آگهی های من" , max_length=20)
    my_channel = models.CharField("کانال های من" ,  max_length=20)
    last_seen = models.CharField("آخرین بازدید" ,  max_length=20)

    pay = models.CharField( "صورت حساب" , max_length=20)
    saved = models.CharField("ذخیره شده ها" , max_length=20)



