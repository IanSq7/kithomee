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
    #if request.method == "POST":
    #  form = CustomUserCreationForm(request.POST)
    # if form.is_valid():
        #    form.save()
        #   username = form.cleaned_data.get("username")
        #  messages.success(request, f"Account created for {username}!")
        # return redirect("inicio")
    #else:
    #   form = CustomUserCreationForm()
    # return render (request, 'menu/register.html', {"form": form})


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

def escritoriodetalle1 (request):
    return render (request, 'menu/escritoriodetalle1.html')

def escritoriodetalle2 (request):
    return render (request, 'menu/escritoriodetalle2.html')

def roperos (request):
    return render (request, 'menu/roperos.html')

def roperodetalle1 (request):
    return render (request, 'menu/roperodetalle1.html')

def roperodetalle2 (request):
    return render (request, 'menu/roperodetalle2.html')

def sillasoficina (request):
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
# inicio se sesion / cierre de sesion




