from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('add/<int:product_id>/', add_product, name='add_product'),  
    path('remove/<int:product_id>/', remove_product, name='remove_product'),
    path('decrement/<int:product_id>/', decrement_product, name='decrement_product'),
    path('clear/', clear_cart, name='clear_cart'),
]