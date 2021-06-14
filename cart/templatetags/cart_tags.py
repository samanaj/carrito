from django import template
"""
 los templetags sirven para crear filtros en las templates
 por ejemplo podemos utilizar un filtro para multiplicar valores y otro para formatos de dinero
 para ello importamos de django el template para poder utilizar register
"""
register = template.Library()

#usaamos el register como un decorador de tipo filtro.
@register.filter()
# creamos la funcion multiplicar recibe un value y un argumento
def multiply(value, arg):
    #multimplicamos value por el argumento y el resultado puede ser un decimal
    return float(value) * arg


@register.filter()
#formato de moneda
def money_format(value, arg):
    #la f de formato
    return f"{value}{arg}"

"""
con esto creado vamos a el listado de productos a implementarlos.
"""