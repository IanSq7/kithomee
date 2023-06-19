from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    
    username = data['usuario']
    password = data['contrasena']
    try:
        user = user.objects.get(username=username)
    except user.DoesNotExist:
        return Response("Usuario invalido")
    # validacion
    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Contraseña incorrecta")
    
    #crear o recuperar el token
    token, created = Token.objects.get_or_create(user=user)
    return Response(token.key)