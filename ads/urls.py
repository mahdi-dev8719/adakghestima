from django.urls import path
from .views import AdList , AdDetail



urlpatterns = [
    path('ad/', AdList.as_view(), name="ad"),
    path('ad/<slug:slug>', AdDetail.as_view(), name="ad-detail"),
    # path('add/page/<int:page>' ,ProductListView.as_view() , name =""
]