from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView



# Create your views here.
def home (request):
    return render(request,'menu/home.html')

def about (request):
    return render (request, 'menu/about.html')

def adminvista (request):
    return render (request, 'menu/adminvista.html')

def banqueta (request):
    return render (request, 'menu/banqueta.html')

def changepassword (request):
    return render (request, 'menu/changepassword.html')

def checkit (request):
    return render (request, 'menu/checkit.html')

def comoda (request):
    return render (request, 'menu/comoda.html')

def contact (request):
    return render (request, 'menu/contact.html')

def lampara (request):
    return render (request, 'menu/lampara.html')

def lamparatecho (request):
    return render (request, 'menu/lamparatecho.html')

def perfil (request):
    return render (request, 'menu/perfil.html')

def recovery (request):
    return render (request, 'menu/recovery.html')

def register (request):
    return render (request, 'menu/register.html')


def shop (request):
    return render (request, 'menu/shop.html')

def silla (request):
    return render (request, 'menu/silla.html')

def sitial (request):
    return render (request, 'menu/sitial.html')

def sofa1 (request):
    return render (request, 'menu/sofa1.html')

def sofaredondo (request):
    return render (request, 'menu/sofaredondo.html')

def team (request):
    return render (request, 'menu/team.html')

def sofahogar (request):
    return render (request, 'menu/sofahogar.html')

def sofahogardetalle (request):
    return render (request, 'menu/sofahogardetalle.html')

def escritorios (request):
    return render (request, 'menu/escritorios.html')

def escritoriodetalle (request):
    return render (request, 'menu/escritoriodetalle.html')

def escritoriodetalle1 (request):
    return render (request, 'menu/escritoriodetalle1.html')

def roperos (request):
    return render (request, 'menu/roperos.html')

def roperodetalle1 (request):
    return render (request, 'menu/roperodetalle1.html')

def roperodetalle2 (request):
    return render (request, 'menu/roperodetalle2.html')

def sillasoficinas (request):
    return render (request, 'menu/sillasoficina.html')

def sillaoficinadetalle1 (request):
    return render (request, 'menu/sillaoficinadetalle1.html')

def sillaoficinadetalle2 (request):
    return render (request, 'menu/sillaoficinadetalle2.html')

def veladores (request):
    return render (request, 'menu/veladores.html')

def veladordetalle1 (request):
    return render (request, 'menu/veladordetalle1.html')

def veladordetalle2 (request):
    return render (request, 'menu/veladordetalle2.html')

#CARRITO DE COMPRAS
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
        
# inicio se sesion / cierre de sesion



# def user_login(request):
    '''
    Login
    '''
    #if request.method == 'POST':
    ##        user = authenticate(
    #           username=request.POST['email'],
    #          password=request.POST['password']
    #     )
        #    if user is not None:
        #       login(request, user)
        #       return redirect(dashboard)
        