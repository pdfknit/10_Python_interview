from django.db import models
from django.utils.timezone import now


# В каталоге приложения создать модель, которая должна хранить информацию о поступивших товарах:
# название, дату поступления, цену, единицу измерения, имя поставщика. Выполнить миграции.

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

    def __str__(self):
        return f'{self.name} {self.price}{self.unit}'
