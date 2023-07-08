from django.urls import path, include
from rest_pregunta.views import lista_pregunta, detalle_pregunta
from rest_pregunta.viewslogin import login
from rest_framework import routers
from rest_pregunta import views

router=routers.DefaultRouter()
router.register(r'pregunta',views.PreguntaViewSet)


urlpatterns = [
    path('',include(router.urls)),
    #path('lista_pregunta', lista_pregunta, name="lista_pregunta"),
    #path('detalle_pregunta/<id>', detalle_pregunta, name="detalle_pregunta"),
    #path('login',login, name="login"),

]