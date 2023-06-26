from menu import models

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
    
    #AÑADIR PRODUCTO
    def add(self, Producto):
        if str(Producto) not in self.cart.keys():
            self.cart[Producto.id] = {
                "product_id": Producto.name,
                "name": Producto.name,
                "quantity": 1,
                "price": str(Producto.price),
                "image": Producto.image.url
            }
        else:
            for key, value in self.cart.items():
                if key == str(Producto.id):
                    value["quantity"] = value["quantity"] + 1
                    break
        self.save()

    #GUARDAR PRODUCTOS EN SESSION
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    #ELIMINAR PRODUCTOS
    def remove(self, Producto):
        Producto_id = str(Producto.id)
        if Producto_id in self.cart:
            del self.cart[Producto_id]
            self.save()

    #REDUCIR LA CANTIDAD DE PRODUCTOS
    def decrement(self, Producto):
        for key, value in self.cart.items():
            if key == str(Producto.id):
                value["quantity"] = value["quantity"] - 1
                if value["quantity"] < 1:
                    self.remove(Producto)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")

    #INICIAR CON EL CARRITO VACIO
    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True
