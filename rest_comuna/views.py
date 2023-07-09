from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ComunaSerializer
from menu.models import Comuna
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer




@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_comuna(request):
    if request.method == 'GET':
        comuna=Comuna.objects.all()
        serializer=ComunaSerializer(comuna, many=True)
        return Response(serializer.data)           
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ComunaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
      	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# ORDEN DE LOS PUT... Y USO DE IF

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_comuna (request, id):
    try: 
        Comuna=Comuna.objects.get(idComuna=id)
    except Comuna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=ComunaSerializer(Comuna)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parser(request)
        serializer = ComunaSerializer(Comuna, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Comuna.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here. aqui van los de las rest
# Faltan delete y put



