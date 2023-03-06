from rest_framework import serializers

from .models import Category , SubCategory

class CategoriesSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='category.title')
    class Meta:
        model = Category
        fields = ('title',)

class CategorySerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Category
    #     fields = ('id','children' )

    pass