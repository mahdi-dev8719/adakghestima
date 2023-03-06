from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Category , SubCategory
from django.core.paginator import Paginator
from .seializers import CategorySerializer , CategoriesSerializer
from rest_framework.response import Response
from django.views.generic.list import ListView

class CategoryListView(APIView):
    def get(self, request, page=1):
        categories = Category.objects.all()
        paginator = Paginator(categories, 24)
        page = request.GET.get('page')
        category = paginator.get_page(page)
        serializer = CategoriesSerializer(category, many=True)

        return Response(serializer.data)

class ChildrenListView(APIView):
        # paginate_by = 24
        # def get_queryset(self):
        #     slug = self.kwargs.get('slug')
        #     category = get_object_or_404(Category.objects.all() , slug = slug)
        #     return category.product.all()
    pass


#     def get(self,request , page=1):
#         categories = SubCategory.objects.all()
#         paginator = Paginator(categories, 24)
#         page = request.GET.get('page')
#         category = paginator.get_page(page)
#         serializer = CategorySerializer(category,many=True)
#         return Response(serializer.data)
#
