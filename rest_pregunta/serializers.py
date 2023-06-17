from rest_framework import serializers
from menu.models import Pregunta

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ['idPregunta','nombre']