from shop.models import (
    Productos,
    Categorias,
    ProductosCategorias,
    Proveedores,
    Movimientos,
    DetallesMovimientoProducto,
    )
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer , SerializerMethodField

class ProductosSerializer(ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class CategoriasSerializer(ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'

class ProductosCategoriasSerializer(ModelSerializer):
    class Meta:
        model = ProductosCategorias
        fields = '__all__'
        
class ProveedoresSerializer(ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'
    

class MovimientosSerializer(ModelSerializer):
    class Meta:
        model = Movimientos
        fields = '__all__'

class DetallesMovimientoProductoSerializer(ModelSerializer):
    class Meta:
        model = DetallesMovimientoProducto
        fields = '__all__'