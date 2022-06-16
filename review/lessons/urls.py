# from django.conf.urls import url
from lessons.views import ProductListView
import lessons.views as lessons

from django.urls import path


urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products2/', lessons.products, name='product'),
    path('category/<int:pk>/', lessons.products_in_categories, name='categories'),
]
