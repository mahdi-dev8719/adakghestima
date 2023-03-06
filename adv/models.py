from django.db import models
from django.conf import settings


class Adv(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField("عنوان", max_length=20 )
    desc = models.TextField('توضیحات',max_length=1024)
    cover = models.ImageField("عکس اصلی", upload_to='')
    plan = models.ImageField("عکس ها", upload_to='')
    start_day = models.CharField("سال", max_length=20)
    end_day = models.IntegerField('قیمت',default=0)

    class Meta:
        verbose_name = 'تبلیغات'
        verbose_name_plural = 'پلن های تبلیغاتی'

class Plan(models.Model):
    pass