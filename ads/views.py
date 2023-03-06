from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.template import loader
from rest_framework.renderers import JSONRenderer
from django.db import models
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from .models import Ad
from .serializers import AdSerializer


class AdList(ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', 'price' , 'sell_type' , 'type' , 'city' , 'state' , 'title' )

class AdDetail(RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    lookup_field = 'slug'


#
# #
# class ProductListView(viewsets.ModelViewSet):
#     queryset = Ad.objects.all()
#     serializer_class = AdSerializer
#
#     # def get_queryset(self):
#     #     return self.request.user.accounts.all()
#     #
#     # def get(self,request , page=1):
#     #     products = Ad.objects.all()
#     #     paginator = Paginator(products, 24)
#     #     page = request.GET.get('page')
#     #     product = paginator.get_page(page)
#     #     serializer = AdSerializer(product,many=True)
#     #     return Response(serializer.data)
#
#
# class AdvList(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#
#     # def list(self, request):
#     #     queryset = Ad.objects.all()
#     #     serializer = AdSerializer(queryset, many=True)
#     #     context = {"product": Response(serializer.data)}
#     #     return render(request, 'ad.html', context)
#
#     def list(self, request, pk=None):
#         queryset = Ad.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = AdSerializer(user)
#         return Response(serializer.data)
#
#     # class AdList()
#
#     def retrieve(self, request, pk=None):
#         queryset = Ad.objects.all()
#         ad = get_object_or_404(queryset, pk=pk)
#         serializer = AdSerializer(ad)
#         return Response(serializer.data)

    #
    # class AdViewSet(viewsets.ViewSet):
    #
    #     def list(self, request):
    #         pass
    #
    #     def create(self, request):
    #         pass
    #
    #     def retrieve(self, request, pk=None):
    #         pass
    #
    #     def update(self, request, pk=None):
    #         pass
    #
    #     def partial_update(self, request, pk=None):
    #         pass
    #
    #     def destroy(self, request, pk=None):
    #         pass
    #
    #

