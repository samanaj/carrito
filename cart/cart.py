class Cart:
    # metodo constructor de la clase, le pasamos el self y el request, el cual sera siempre el de la petición actual
    def __init__(self, request):
        # inicializamos variables
        self.request = request
        self.session = request.session
        # definimos una variable para trabajar con el carrito
        # igualamos la variable cart a la session que podamos tener en el carrito
        cart = self.session.get("cart")
        # comparamos si no tenemos el carrito
        if not cart:
            # si no hay carrito hacemos lo siguiente
            # la inicializamos con un diccionario y de esta manera ya tenemos lista la variable cart para poder utilizarla
            cart =self.session["cart"] = {}
        # si tenemos el carrito solamente lo inicializamos
        self.cart = cart
    
    def add(self, product):        
        #aca comprobamos si el producto esta en el carrito
        if str(product.id) not in self.cart.keys():
            # si no esta lo añadimos por medio de un diccionario
            self.cart[product.id]= {
                "product.id": product.id,
                "name" : product.name,
                "quantity": 1,
                "price": str(product.price),
                "image": product.image.url
            }
        # si el producto esta en el carrito utilizamos un for para recorrer todos los items del carrito
        else:
            for key, value in self.cart.items():
                # comprobamos si la key (que es la clave que viene del diccionario)es igual al id del producto
                if key == str(product.id):
                    # si esto se cumple incrementamos la cantidad en el carrito
                    value["quantity"] = value["quantity"]+1
                    break
        self.save()
    #definimos el metodo para almacenar las sesiones del carrito
    def save(self):
        # guardamos el carrito
        self.session["cart"] = self.cart
        # esta es la forma de decirle en django que la session a sido actualizada.
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def drecrement(self, product):
        #recorremos los items que hay en el carrito
        for key, value in self.cart.items():
            #si hay una coincidencia, comparamos la clave con el valor del id
            if key == str(product.id):
                #modificamos la cantidad con value["quantity"]
                value["quantity"] = value["quantity"] - 1
                #comprobamos si la cantidad es menor a 1 esto con el fin de que eliminar el producto del carrito
                if value["quantity"] < 1:
                    self.remove(product)
                else:
                    #guardamos en el caso de que todavia existen productos en el carrito
                    self.save()
                break
            #si el producto no esta 
            else:
                print("El producto no existe en el carrito")

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True
