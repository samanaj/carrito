from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cart.cart import Cart
from .models import Product

# Create your views here.

@login_required(login_url='/autenticacion/acceder')
#vista basada en funciones
def listado_productos(request):
    #esto es porque en el context_processor estamos recorriendo los items del cart y si no lo hemos inicialidzado 
    #obtendremos un error    
    cart = Cart(request)
    #accedemos a todos los productos que tenemos en la base de datos
    products = Product.objects.all()
    #aqui tenemos un return de render y le pasamos el request, y el template en este caso products(carpeta donde esta) /listado.html (nombre del archivo)

    return render(request, "products/listado.html", {
        #tambien le pasamos un diccionario con los productos la clave "produtcs" tendra todos los productos de la consulta.
        "products": products
    })
