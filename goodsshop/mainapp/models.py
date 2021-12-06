from django.db import models
from uuid import uuid4
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class Catalog(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=128, verbose_name='Название каталога')
    site = models.ManyToManyField(Site, null=True)
    objects = models.Manager()
    on_site = CurrentSiteManager()

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    def __str__(self):
        return self.name


class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    catalogs = models.ManyToManyField(Catalog, related_name='products', blank=True, verbose_name='Каталог')
    name = models.CharField(max_length=128, verbose_name='Название товара')
    delivery_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    unit_of_measure = models.CharField(max_length=64, verbose_name='Единица измерения')
    producer = models.CharField(max_length=256, verbose_name='Производитель')
    image = models.ImageField(upload_to='product_images', null=True, verbose_name='Изображение товара')
    site = models.ManyToManyField(Site)
    objects = models.Manager()
    on_site = CurrentSiteManager()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-delivery_date']

    def __str__(self):
        return self.name
