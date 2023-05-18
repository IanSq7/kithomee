from django.contrib import admin
from django.urls import path, include
from .views import home, about, adminvista,banqueta,changepassword,checkit,comoda,contact,lampara,lamparatecho,perfil,recovery,register,shop,silla,sitial,sofa1,sofaredondo,team
urlpatterns = [
    path('',home,name="home"),
    path('about/',about,name="about"),
    path('adminvista/', adminvista,name="adminvista"),
    path('banqueta/',banqueta,name="banqueta"),
    path('changepassword/',changepassword,name="changepassword"),
    path('checkit/',checkit,name="checkit"),
    path('comoda/',comoda,name="comoda"),
    path('contact/',contact,name="contact"),
    path('lampara/',lampara,name="lampara"),
    path('lamparatecho/',lamparatecho,name="lamparatecho"),
    path('perfil/',perfil,name="perfil"),
    path('recovery/',recovery,name="recovery"),
    path('register/',register,name="register"),
    path('shop/',shop,name="shop"),
    path('silla/',silla,name="silla"),
    path('sitial/',sitial,name="sitial"),
    path('sofa1/',sofa1,name="sofa1"),
    path('sofaredondo/',sofaredondo,name="sofaredondo"),
    path('team/',team,name="team")


]
