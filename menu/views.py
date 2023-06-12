from django.shortcuts import render
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
    
# inicio se sesion / cierre de sesion


