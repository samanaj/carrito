from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from products.models import Product
from .cart import Cart
# Create your views here.

@login_required(login_url="/autenticacion/login")
def add_product(request, product_id):
    # crea el carrito
    cart = Cart(request)
    # busca el producto con el id que le pasemos
    product = Product.objects.get(id=product_id)
    # lo añade al carrito, y si existe lo incrementa
    cart.add(product=product)
    # redireccionamos a listaod de producot
    return redirect("products:listado_productos")

@login_required(login_url="/autenticacion/login")
def remove_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect("products:listado_productos")

@login_required(login_url="/autenticacion/login")
def decrement_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.drecrement(product=product)
    return redirect("products:listado_productos")

@login_required(login_url="/autenticacion/login")
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("products:listado_productos")