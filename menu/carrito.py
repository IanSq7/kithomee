from menu import models
#INICIALIZADOR
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito=self.session["carrito"] = {}
        else:
            self.carrito = carrito
    
    #AÑADIR PRODUCTO
    def agregar(self, Producto):
        if(str(Producto.id) not in self.carrito.keys()):
            self.carrito[Producto.id]={
                "producto_id":Producto.id,
                "nombre":Producto.nombre,
                "precio":str(Producto.precio),
                "cantidad":1,
                "imagen":Producto.foto.url
            }
        else:
            for key, value in self.carrito.items():
                if key==str(Producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    break
        self.guardar_carrito()
        

    #GUARDAR PRODUCTOS EN SESSION
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    #ELIMINAR PRODUCTOS
    def eliminar(self, Producto):
        Producto.id = str(Producto.id)
        if Producto.id in self.carrito:
            del self.carrito[Producto.id]
            self.guardar_carrito()

    #REDUCIR LA CANTIDAD DE PRODUCTOS
    def restar(self, Producto):
        for key, value in self.carrito.items():
            if key==str(Producto.id):
                value["cantidad"]=value["cantidad"]-1
                if value["cantidad"]<1:
                    self.eliminar(Producto)
                break
        self.guardar_carrito()

    #INICIAR CON EL CARRITO VACIO
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
