from django.contrib import admin
from django.urls import path, include
from .views import home, about, adminvista,banqueta,changepassword,checkit,comoda,contact,lampara,lamparatecho,perfil,recovery,register,shop,silla,sitial,sofa1,sofaredondo,team,sofahogar,sofahogardetalle,escritorios,escritoriodetalle,escritoriodetalle1,roperos,roperodetalle1,roperodetalle2,sillasoficinas,sillaoficinadetalle1,sillaoficinadetalle2,veladores,veladordetalle1,veladordetalle2
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
    path('team/',team,name="team"),
    path('sofahogar/',sofahogar,name="sofahogar"),
    path('sofahogardetalle/',sofahogardetalle,name="sofahogardetalle"),
    path('escritorios/',escritorios,name="escritorios"),
    path('escritoriodetalle/',escritoriodetalle,name="escritoriodetalle"),
    path('escritoriodetalle1/',escritoriodetalle1,name="escritoriodetalle1"),
    path('roperos/',roperos,name="roperos"),
    path('roperodetalle1/',roperodetalle1,name="roperodetalle1"),
    path('roperodetalle2/',roperodetalle2,name="roperodetalle2"),
    path('sillasoficinas/',sillasoficinas,name="sillasoficinas"),
    path('sillaoficinadetalle1/',sillaoficinadetalle1,name="sillaoficinadetalle1"),
    path('sillaoficinadetalle2/',sillaoficinadetalle2,name="sillaoficinadetalle2"),
    path('veladores/',veladores,name="veladores"),
    path('veladordetalle1/',veladordetalle1,name="veladordetalle1"),
    path('veladordetalle2/',veladordetalle2,name="veladordetalle2")


]
