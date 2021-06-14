"""
son variables globales que las podemos utilizar dentro de todas las templates en django a nivel de proyecto
los context processor
"""

#definmos una funcion que recibe el request
def cart_total_amount(request):
    #inciamos el total en 0
    total = 0.0
    #verificamois que el usuario este autenticado
    if request.user.is_authenticated:
        #si esta autenticado recorreomos los items comprobando que la clave y el valor esten en la sesion del carrito
        for key, value in request.session['cart'].items():
            #si esto esta realizamos el calculo del total
            total = total + (float(value['price']) * value['quantity'])
    #retornamos un diccionario con la funcion como clave y el total como valor.
    return {'cart_total_amount': total}

"""
una vez terminado debemos de registrar esta funcion global en el settings en la parte de 
templates. de esta manera  
'cart.context_processor.cart_total_amount',
de esta manera la podemos llamar en todas las templates. podemos probarlo en listado productos.
pero antes debemos de hacer un pequeño cambio en la app productos vistas
"""