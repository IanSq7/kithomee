from rest_framework import serializers
from kithomee.products.models import Producto

class ProductoSerializers(serializers.modelSerialzer):
    class Meta:
        model = Productofields = '__all__'