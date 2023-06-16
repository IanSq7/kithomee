from django.urls import path 
from rest_pregunta.views import lista_comuna, detalle_comuna
from rest_pregunta.viewslogin import login


urlpatterns = [
    path('lista_comuna',lista_comuna, name="lista_comuna"),
    path('detalle_comuna/<id>', detalle_comuna, name="detalle_comuna"),
    path('login',login, name="login"),

]