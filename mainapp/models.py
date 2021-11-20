from django.db import models
from uuid import uuid4


class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=128, verbose_name='Название товара')
    delivery_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    unit_of_measure = models.CharField(max_length=64, verbose_name='Единица измерения')
    producer = models.CharField(max_length=256, verbose_name='Производитель')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-delivery_date']

    def __str__(self):
        return self.name
