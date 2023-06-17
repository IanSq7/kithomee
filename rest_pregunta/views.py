from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import PreguntaSerializer
from menu.models import Pregunta
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_pregunta(request):
    if request.method == 'GET':
        comuna=Pregunta.objects.all()
        serializer=PreguntaSerializer(comuna, many=True)
        return Response(serializer.data)           
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PreguntaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
      	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_pregunta(request, id):
    try: 
        Pregunta=Pregunta.objects.get(idPregunta=id)
    except Pregunta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=PreguntaSerializer(Pregunta)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parser(request)
        serializer = PreguntaSerializer(Pregunta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Pregunta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.
