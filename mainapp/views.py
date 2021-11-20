from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class GoodsListView(ListView):
    model = Product
    queryset = Product.objects.all()
