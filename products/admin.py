from django.contrib import admin
#importamos los modelos
from .models import Category, Product
# Register your models here.
#registramos todos los modelos que necesitemos
admin.site.register([Category, Product])