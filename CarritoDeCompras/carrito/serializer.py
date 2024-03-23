from rest_framework import serializers
from .models import Producto, Tienda, Precio

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = '__all__'

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = '__all__'