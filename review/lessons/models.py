from django.db import models
from django.utils.timezone import now


# Добавить в приложение каталога модель Раздел каталога.
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(max_length=128, verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    UNIT_CHOICES = (
        ('peace', 'штук'),
        ('pack', 'упаковка'),
        ('kg', 'кг'),

    )

    name = models.CharField(max_length=30)
    arrive = models.DateTimeField(default=now, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена', default=0)
    unit = models.CharField(max_length=30, verbose_name="Единица измерения", choices=UNIT_CHOICES)
    supplier = models.CharField(max_length=50, verbose_name="Поставщик")
    # Модифицировать модель товара, добавив возможность включать ее в один или несколько разделов.
    categories = models.ManyToManyField(ProductCategory, verbose_name="Категории")

    def __str__(self):
        return f'{self.name} — {self.price} за {self.unit}'
