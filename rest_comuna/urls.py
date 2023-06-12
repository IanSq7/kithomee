from django.urls import path 
from rest_comuna.views import lista_comuna

urlpatterns = [
    path('lista_comuna',lista_comuna, name="lista_comuna")

]