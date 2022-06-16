from django.shortcuts import render
from django.views.generic.list import ListView
from lessons.models import Product
from django.shortcuts import render


class ProductListView(ListView):
    model = Product
    template_name = "lessons/table.html"

    def get_queryset(self):
        products = Product.objects.all()
        return products


def products(request):
    products = Product.objects.all()
    data = {"products": products}
    return render(request, "lessons/goods_list.html", context=data)
