from django.db import models
from django.conf import settings
from category.models import Category
from django.contrib.auth.models import User



class Ad(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='user')
    category = models.ForeignKey(Category, on_delete=models.PROTECT , related_name="product")
    slug = models.SlugField(default="", null=False,max_length=100, unique=True, verbose_name='آدرس محصول')
    title = models.CharField("عنوان", max_length=20)
    desc = models.TextField('توضیحات', max_length=1024)
    price = models.IntegerField('قیمت', default=0)
    cover = models.ImageField("عکس اصلی", upload_to='image/product/',null=True,blank=True)
    image = models.ImageField("عکس ها", upload_to='images/product/',null=True,blank=True)
    image_voice = models.ImageField("عکس صوتی", upload_to='voice-image/product/',null=True,blank=True)
    video = models.FileField("فیلم", upload_to="video/product/",null=True,blank=True)
    voice = models.FileField("صوت", upload_to="voice/product/",null=True,blank=True)
    year = models.CharField("سال", max_length=20)
    state = models.CharField("استان", max_length=20,null=True,blank=True)
    city = models.CharField("شهر", max_length=20,null=True,blank=True)
    sell_type = models.CharField("نوع فروش", max_length=20,null=True,blank=True)

    type = models.CharField('نوع آگهی', max_length=30)
    is_show = models.BooleanField('تایید آگهی',default=False,null=True,blank=True)
    created_time = models.DateTimeField('زمان انتشار',auto_now_add=True)
    updated_time = models.DateTimeField('زمان بروزرسانی',auto_now=True)

    class Meta:
        verbose_name = 'آگهی'
        verbose_name_plural = 'آگهی ها '


    def __str__(self):
        return self.title


class Car(Ad):
    brand = models.CharField("برند", max_length=20, null=False, blank=True)
    model = models.CharField("مدل", max_length=20, null=False, blank=True)
    color = models.CharField("رنگ", max_length=20, null=True, blank=True)
    body = models.CharField("بدنه", max_length=20, null=True, blank=True)
    func = models.CharField("کارکرد", max_length=20, null=True, blank=True)
    engine = models.CharField("موتور", max_length=20, null=True, blank=True)
    chassis = models.CharField("شاسی", max_length=20, null=True, blank=True)
    insurance = models.CharField("بیمه", max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = 'آگهی ماشین'
        verbose_name_plural = 'آگهی های ماشین '


    def __str__(self):
        return self.title
#
# class NewAd(models.Model):
#     ads = models.ForeignKey(to=Ads,on_delete = models.CASCADE,related_name="AdDetail")
#     title = models.CharField("عنوان", max_length=20)
#     desc = models.TextField('توضیحات',max_length=1024)
#     price = models.IntegerField('قیمت',default=0)
#     cover = models.ImageField("عکس اصلی", upload_to='')
#     image = models.ImageField("عکس ها", upload_to='')
#     image_voice = models.ImageField("عکس و صوت", upload_to='')
#     video = models.FileField("فیلم", upload_to="")
#     voice = models.FileField("صوت", upload_to="")
#     state = models.CharField("استان", max_length=20)
#     city = models.CharField("شهر", max_length=20)
#     sell_type = models.CharField("نوع فروش", max_length=20)
#     brand = models.CharField("برند", max_length=20)
#     year = models.CharField("سال", max_length=20)
#     color = models.CharField("رنگ", max_length=20)
#     body = models.CharField("بدنه", max_length=20)
#     engine = models.CharField("موتور", max_length=20)
#     chassis = models.CharField("شاسی", max_length=20)
#     insurance = models.CharField("بیمه", max_length=20)
#     is_show = models.BooleanField('تایید آگهی',default=False)
#     created_time = models.DateTimeField('زمان انتشار',auto_now_add=True)
#     updated_time = models.DateTimeField('زمان بروزرسانی',auto_now=True)
#
#
#     class Meta:
#         verbose_name = 'افزودن آگهی'
#         verbose_name_plural = 'آگهی های نو'
#
# class AdDetail(models.Model):
#     title = models.CharField("عنوان", max_length=20 )
#     desc = models.TextField('توضیحات',max_length=1024)
#     cover = models.ImageField("عکس اصلی", upload_to='')
#     image = models.ImageField("عکس ها", upload_to='')
#     year = models.CharField("سال", max_length=20)
#     price = models.IntegerField('قیمت',default=0)
#
#     class Meta:
#         verbose_name = 'جزئیات آگهی'
#         verbose_name_plural = 'جزئیات '

class PriceEstimate(models.Model):
    ad = models.ForeignKey(to=Ad , on_delete=models.CASCADE)

    low = models.CharField("پایین" , max_length=200)
    mid = models.CharField("منصفانه" , max_length=200)
    high = models.CharField("بالا" , max_length=200)

    function = models.IntegerField("میزان کارکرد" ,default=0)
    body_status = models.IntegerField("وضعیت بدنه" ,default=0)
    chassis = models.IntegerField("وضعیت شاسی ها" ,default=0)
    color = models.CharField("رنگ",max_length=100)
    year = models.IntegerField("سال تولید",default=0)

    estimate_price = 0
    current_price = 0
    result_price = 0

    class Meta:
        verbose_name = 'قیمت منصفانه'
        verbose_name_plural = 'نوع قیمت'