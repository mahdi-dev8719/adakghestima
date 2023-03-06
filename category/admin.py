from django.contrib import admin
from django.apps import apps
from .models import Category , SubCategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title', 'slug', "status" , 'parent')
    list_filter = (['status'])
    search_fields= ('title' , 'slug')
    prepopulated_fields = {'slug': ("title",)}

admin.site.register(Category, CategoryAdmin)

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug' , 'status')
#     search_fields = ('title', 'desc')
#     prepopulated_fields = {'slug': ('title',)}
#
#     def category_to_str(self,obj):
#         return " ".join([category.title for category in obj.category.published()])
#     category_to_str.short_description = 'دسته بندی'
#
# admin.site.register(Product , ProductAdmin)
