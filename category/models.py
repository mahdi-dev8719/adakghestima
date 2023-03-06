from django.db import models

# class ProductManager(models.Manager):
#     def published(self):
#         return self.filter(status='p')

# CAT_CHOICES = (
#     ("car", "CAR"),
#     ("moto", "MOTO"),
#     ("tools", "TOOLS")
# )


class Category(models.Model):
    parent = models.ForeignKey('self',default=None,null=True ,blank=True, on_delete=models.SET_NULL , related_name='children',verbose_name='زیر دسته' )
    title = models.CharField(max_length=200 , verbose_name="عنوان دسته بندی")
    slug = models.SlugField(default="",null=False,max_length=100, unique=True, verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="نمایش؟")
    position = models.IntegerField(default=0,verbose_name="شمارش" , unique=True , )

    def __str__(self):
        return(f'{ self.title }')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['position']



    # def category_published(self):
    #     return self.category.filter(status=True)

class SubCategory(models.Model):
    # STATUS_CHOICES = (
    #     ("d", "پیش نویس"),
    #     ("p",'منتشر شده')
    # )
    # status = models.BooleanField(default=True, verbose_name="نمایش؟" , choices=STATUS_CHOICES)
    # title = models.CharField(max_length=200, verbose_name="دسته بندی محصول")
    # slug = models.SlugField(default="", null=False,max_length=100, unique=True, verbose_name='آدرس دسته بندی')
    # position = models.IntegerField(verbose_name="شمارش" , unique=True , )
    # category = models.ManyToOneRel(to=Category,field_name="",field="", related_name="sub-category")
    # # choices = models.Choices(STATUS_CHOICES)
    #
    #
    # class Meta:
    #     verbose_name = 'دسته بندی'
    #     verbose_name_plural = 'دسته بندی ها'
    #
    # def __str__(self):
    #     return self.title
    #

    pass

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
#
# class Category(models.Model):
#     name = models.CharField(max_length=200)
#     slug = models.SlugField()
#     parent = models.ForeignKey('self', blank=True, null=True, related_name='children',on_delete=models.SET_NULL)
#
#     class Meta:
#         # enforcing that there can not be two categories under a parent with same slug
#
#         # __str__ method elaborated later in post.  use __unicode__ in place of
#
#         # __str__ if you are using python 2
#
#         unique_together = ('slug', 'parent',)
#         verbose_name = 'افزودن آگهی'
#         verbose_name_plural = "categories"
#         # ordering = ['price' , '-price']
#
#     def __str__(self):
#         full_path = [self.name]
#         k = self.parent
#         while k is not None:
#             full_path.append(k.name)
#             k = k.parent
#         return ' -> '.join(full_path[::-1])
#
#
# class VehiclesCate(models.Model):
#     name = models.CharField(max_length=200)
#     slug = models.SlugField()
#     parent = models.ForeignKey('category', blank=True, null=True, related_name='vehicles',on_delete=models.SET_NULL)
#
#
# class CarCategory(models.Model):
#     name = models.CharField("ماشین",max_length=200)
#     slug = models.SlugField()
#     parent = models.ForeignKey('VehiclesCate', blank=True, null=True, related_name='car', on_delete=models.SET_NULL)
#
#     def __str__(self):
#         return self.title
# class MotoCategory(models.Model):
#     name = models.CharField("موتور",max_length=200)
#     slug = models.SlugField()
#     parent = models.ForeignKey('VehiclesCate', blank=True, null=True, related_name='moto', on_delete=models.SET_NULL)
#
#     def __str__(self):
#         return self.title
# class PartsCategory(models.Model):
#     name = models.CharField("لوازم یدکی",max_length=200)
#     slug = models.SlugField()
#     parent = models.ForeignKey('VehiclesCate', blank=True, null=True, related_name='spare_parts', on_delete=models.SET_NULL)
#
#     def __str__(self):
#         return self.title
# class BoatCategory(models.Model):
#     name = models.CharField("قایق",max_length=200)
#     slug = models.SlugField()
#     parent = models.ForeignKey('VehiclesCate', blank=True, null=True, related_name='boat', on_delete=models.SET_NULL)
#
#     def __str__(self):
#         return self.title
