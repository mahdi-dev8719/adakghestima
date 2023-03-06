from django.urls import path
from .views import CategoryListView , ChildrenListView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name="categories"),
    path('category/', CategoryListView.as_view(), name="categories"),
    path('category/<slug:slug>/page/<int:page>',CategoryListView.as_view() , name ="")

]