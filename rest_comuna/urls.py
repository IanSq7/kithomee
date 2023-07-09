from django.urls import path, include
from rest_comuna.views import lista_comuna, detalle_comuna
from rest_comuna.viewslogin import login
from rest_framework import routers
from rest_comuna import views

router=routers.DefaultRouter()
router.register(r'comuna', views.ComunaSerializer)


urlpatterns = [
    path('',include(router.urls))
    #path('lista_comuna',lista_comuna, name="lista_comuna"),
    #path('detalle_comuna/<id>', detalle_comuna, name="detalle_comuna"),
    #path('login',login, name="login"),

]