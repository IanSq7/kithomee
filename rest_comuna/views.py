from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ComunaSerializer
from menu.models import Comuna
@csrf_exempt
@api_view(['GET','POST'])
def lista_comuna(request):
    if request.method == 'GET':
        comuna=Comuna.objects.all()
        serializer=ComunaSerializer(comuna, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ComunaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
      	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Create your views here. aqui van los de las rest
# Faltan delete y put



