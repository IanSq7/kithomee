from django.urls import path 
from rest_comuna.views import lista_comuna, detalle_comuna

urlpatterns = [
    path('lista_comuna',lista_comuna, name="lista_comuna"),
    path('detalle_comuna/<id>', detalle_comuna, name="detalle_comuna"),


]