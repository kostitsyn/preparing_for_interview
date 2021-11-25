from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Catalog


class GoodsListByCatalog(ListView):
    model = Product
    template_name = 'mainapp/product_by_category.html'

    def get_queryset(self):
        catalog_uuid = self.kwargs.get('pk', None)
        product_by_category = Catalog.objects.get(pk=catalog_uuid).product.all()
        return product_by_category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_catalogs = Catalog.objects.prefetch_related('product').all()
        context['catalogs'] = all_catalogs
        return context


class GoodsListView(ListView):
    model = Product
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_catalogs = Catalog.objects.prefetch_related('product').all()
        context['catalogs'] = all_catalogs
        return context
