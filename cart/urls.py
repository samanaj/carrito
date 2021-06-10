from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('add_product/<int:product_id>/', add_product, name ='add_product'),
    path('remove_product/<int:product_id>/', remove_product, name ='remove_product'),
    path('decrement_product/<int:product_id>/', decrement_product, name ='decrement_product'),

]