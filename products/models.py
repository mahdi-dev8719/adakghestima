# from django.db import models
# from django.conf import settings
# from category.models import Category
#
#
# class Product(models.Model):
#     # user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # category = models.ForeignKey('category.models',on_delete=models.PROTECT)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     # author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField("عنوان", max_length=20)
#     desc = models.TextField('توضیحات', max_length=1024)
#     price = models.IntegerField('قیمت', default=0)
#     cover = models.ImageField("عکس اصلی", upload_to='image/product/')
#     image = models.ImageField("عکس ها", upload_to='images/product/')
#     image_voice = models.ImageField("عکس صوتی", upload_to='voice-image/product/')
#     video = models.FileField("فیلم", upload_to="video/product/")
#     voice = models.FileField("صوت", upload_to="voice/product/")
#     year = models.CharField("سال", max_length=20)
#     state = models.CharField("استان", max_length=20,null=True,blank=True)
#     city = models.CharField("شهر", max_length=20,null=True,blank=True)
#     sell_type = models.CharField("نوع فروش", max_length=20,null=True,blank=True)
#     brand = models.CharField("برند", max_length=20,null=True,blank=True)
#     model = models.CharField("مدل", max_length=20,null=True,blank=True)
#     color = models.CharField("رنگ", max_length=20,null=True,blank=True)
#     body = models.CharField("بدنه", max_length=20,null=True,blank=True)
#     func = models.CharField("کارکرد", max_length=20,null=True,blank=True)
#     engine = models.CharField("موتور", max_length=20,null=True,blank=True)
#     chassis = models.CharField("شاسی", max_length=20,null=True,blank=True)
#     insurance = models.CharField("بیمه", max_length=20,null=True,blank=True)
#     type = models.CharField('نوع آگهی', max_length=30)
#     is_show = models.BooleanField('تایید آگهی',default=False,null=True,blank=True)
#     created_time = models.DateTimeField('زمان انتشار',auto_now_add=True)
#     updated_time = models.DateTimeField('زمان بروزرسانی',auto_now=True)
#
#     class Meta:
#         verbose_name = 'محصولات'
#         verbose_name_plural = 'آگهی ها'


# CATEGORY = (
#     ("vehicles", "VEHICLES"),
#         ("car" , "CAR"),
#         ("moto" , "MOTO"),
#         ("spare_parts" , "SPARE_PARTS"),
#         ("boat" , "BOAT") ,
#         ("more" , "MORE"),
#
#     ("home", "HOME"),
#         ("Sale", "SALE"),
#             ("apartment", "APARTMENT"),
#             ("villa", "VILLA"),
#             ("earth", "EARTH"),
#
#         ("rent" , "RENT"),
#             ("apartment", "APARTMENT"),
#             ("villa", "VILLA"),
#
#         ("commercial_sales", "COMMERCIAL_SALES"),
#             ("office", "OFFICE"),
#             ("shop", "SHOP"),
#             ("indusrial" , "INDUSTRIAL"),
#
#
#         ("commercial_rent", "COMMERCIAL_RENT"),
#             ("office", "OFFICE"),
#             ("shop", "SHOP"),
#             ("indusrial", "INDUSTRIAL"),
#
#
#         ("short_term_rental"), ("SHORT_TERM_RENTAL")
#             ("apartment", "APARTMENT"),
#             ("villa", "VILLA"),
#             ("office", "OFFICE"),
#
#         ("construction_project") , ("CONSTRUCTION_PROJECT")
#             ("participation", "PARTICIPATION"),
#             ("presell", "PRESELL"),
#
#     ("digital", "DIGITAL"),
#         ("mobile" , "MOBILE"),
#             ("phone" , "PHONE"),
#             ("tablet" , "TABLET"),
#             ("accessories", "ACCESSORIES"),
#             ("simcard" , "SIMCARD"),
#
#         ("computer" , "COMPUTER"),
#             ("mobile_computer", "MOBILE_COMPUTER"),
#             ("desktop_computer", "DESKTOP_COMPUTER"),
#             ("accessories", "ACCESSORIES"),
#             ("network", "NETWORK"),
#             ("printer", "PRINTER"),
#
#     ("console" , "CONSOLE"),
#
#     ("media" , "MEDIA",),
#             ("film_music", "FILE_MUSIC"),
#             ("camera", "CAMERA"),
#             ("player", "PLAYER"),
#             ("home_studio", "HOME_STUDIO"),
#             ("tv", "TV"),
#             ("CCTV", "CCTV"),
#
#     ("telephone" , "TELEPHONE"),
#
#     ("kitchen", "KITCHEN"),
#         ("electric_household", "ELECTRIC_HOUSEHOLD"),
#         ("kitchen_utensils", "KITCHEN_UTENSILS"),
#         ("eating_drinking", "EATING_DRINKING"),
#         ("home_studio", "HOME_STUDIO"),
#         ("tv", "TV"),
#         ("CCTV", "CCTV"),
#
#     ("service", "SERVICE"),
#     ("personal", "PERSONAL"),
#     ("entertainment", "ENTERTAINMENT"),
#     ("social", "SOCIAL"),
#     ("Recruitment", "RECRUITMENT"),
#
# )

#
# class Category(models.Model):
#     category = models.CharField("دسته بندی", max_lenght=200, choices=CAT_CHOICES, default="car",)
