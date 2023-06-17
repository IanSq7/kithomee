from django.urls import path 
from rest_pregunta.views import lista_pregunta, detalle_pregunta
from rest_pregunta.viewslogin import login


urlpatterns = [
    path('lista_pregunta',lista_pregunta, name="lista_pregunta"),
    path('detalle_preguta/<id>', detalle_pregunta, name="detalle_pregunta"),
    path('login',login, name="login"),

]