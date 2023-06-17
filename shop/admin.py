from django.contrib import admin
from .models import Producto,Categoria, ProductoxCategoria, CarroCompras, DetallesProducto
# Register your models here.
admin.site.register([Producto, Categoria, ProductoxCategoria, CarroCompras, DetallesProducto ])