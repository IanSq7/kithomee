from pyexpat.errors import messages

from rest_framework.response import Response
from rest_framework.views import APIView
from menu.carrito import Carrito
from .forms import ProductoForm
from django.contrib.auth.forms import UserCreationForm
from menu.models import Producto
from django.shortcuts import render, redirect
from .forms import LoginForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login





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
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render (request, 'menu/shop.html', data)

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
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect("shop")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect("shop")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto=producto)
    return redirect("shop")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("shop")
        
def add_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario

    return render(request, 'producto/agregar.html', data)

def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }

    return render(request, 'producto/listar.html', data)

# inicio se sesion / cierre de sesion

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request,'menu/shop.html')  # Cambia 'home' por el nombre de la página a la que deseas redirigir después del login
            else:
                form.add_error(None, 'Credenciales inválidas.')
    else:
        form = LoginForm()
    return render(request, 'menu/login.html', {'form': form})


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="about")

        data ["form"] = formulario   
    return render (request, 'menu/registro.html', data)