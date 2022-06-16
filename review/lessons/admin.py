from django.contrib import admin

from .models import Product, ProductCategory

# Register your models here.
admin.site.register(Product)
# Заполнение таблицы разделов и включение в раздел осуществлять через админку сайта.
admin.site.register(ProductCategory)