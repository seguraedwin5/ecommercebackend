from shop.models import Producto
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer , SerializerMethodField

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'