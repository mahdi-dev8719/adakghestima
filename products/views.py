from django.shortcuts import render, redirect
from django.utils import timezone
from rest_framework import request
from .forms import ProductForm

def ProductCreate(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # return redirect('product/detail/', pk=post.pk)
    else:
        form = ProductForm()
        return render(request,'add.html',{'form': form})