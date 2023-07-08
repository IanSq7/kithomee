from django.urls import path, include
from rest_comuna.views import lista_comuna, detalle_comuna
from rest_comuna.viewslogin import login
from rest_framework import routers
from rest_comuna import views


router=routers.DefaultRouter()
router.register(r'comuna',views.ComunaViewSet)


urlpatterns = [
    path('',include(router.urls))
]