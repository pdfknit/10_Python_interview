from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.list import ListView
from lessons.models import Product, ProductCategory
from django.shortcuts import render

all_categories = ProductCategory.objects.all()


class ProductListView(ListView):
    model = Product
    template_name = "lessons/table.html"

    def get_queryset(self):
        products = Product.objects.prefetch_related('categories').all()
        return products


def products(request):

    products = Product.objects.all()
    data = {
        'products': products,
        'all_categories': all_categories,
        'site': get_current_site(request=request),
    }
    return render(request, "lessons/goods_list.html", context=data)


def products_in_categories(request, pk):
    categories = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(categories=categories)

    return render(request, 'lessons/category.html', context={
        'title': 'Категории',
        'products': products,
        'all_categories': all_categories,
        'categories': categories,
        'site': get_current_site(request=request),
    })
