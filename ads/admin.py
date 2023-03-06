from django.contrib import admin
from django.apps import apps

from .models import Ad
# post_models = apps.get_app_config('ads').get_models()
#
# for model in post_models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
# #
# class AdAdmin(admin.ModelAdmin):
#     list_display = '[]'
#     prepopulated_fields = {"slug": ("title", )}
#     def __str__(self):
#         return self.title
# admin.site.register(Ad, AdAdmin)

class AdAdmin(admin.ModelAdmin):
    list_display = ("user" ,
                    "category" ,
                    "title" ,
                    "desc" ,
                    "price" ,
                    "cover" ,
                    "image" ,
                    "image_voice" ,
                    "video",
                    "voice",
                    "year",
                    "state",
                    "city",
                    "sell_type",
                    "is_show",
                    "created_time",
                    "updated_time",
                    )
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Ad, AdAdmin)