# urls.py

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import add_product, product_list,shop_home

urlpatterns = [
    path('add_product/', add_product, name='add_product'),
    path('product_list/', product_list, name='product_list'),
    path('', shop_home, name='shop_home'),

]

