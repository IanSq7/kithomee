from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.backends import BaseBackend


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


def iniciar_session (request):
    usuario=request.POST['usuario']
    contra1=request.POST['contra']
    try:
        user1=user.objects.GET(username=usuario1)
    except user.DoesNotExist:
        messages.error(request, 'El usuario o la contraseña son incorrectos')
        return redirect ('Iniciar')
    
    pass_valida=check_password(contra1,user1.password)
    if not pass_valida:
        messages.error(request,'El usuario o la contraseña son incorrectos')
        
        return redirect ('Iniciar')
    usuario2=usuario.objects.get(username=usuario1,contrasennia=contra1)
    user=authenticate(username=usuario1,password=contra1)
    if user is not None:
        login(request, user)
        if(usuario2.tipousuario.idTipoUsuario == 1):
            return redirect("menu/index.html")
        else:
            contexto = {"usuario":usuario2}
            return render(request,"menu/index.html",contexto)
    else:
        print("B")


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
        
class ProductList(APIView):
    def get(self, request, format=None):
        products = Producto.objects.all()
        serializer = ProductoSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
