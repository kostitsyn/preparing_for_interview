from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Catalog


class Mixin(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_catalogs = Catalog.objects.prefetch_related('products').all()
        context['catalogs'] = all_catalogs
        return context


class GoodsListByCatalog(Mixin):
    model = Product
    template_name = 'mainapp/product_by_category.html'

    def get_queryset(self):
        catalog_uuid = self.kwargs.get('pk', None)
        product_by_category = Catalog.objects.get(pk=catalog_uuid).products.all()
        return product_by_category


class GoodsListView(Mixin):
    model = Product
    queryset = Product.objects.all()
