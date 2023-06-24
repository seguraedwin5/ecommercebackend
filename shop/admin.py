from django.contrib import admin
from .models import (
    Productos,
    Categorias,
    ProductosCategorias,
    Proveedores,
    Movimientos,
    DetallesMovimientoProducto,
    )

# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    model = Productos
    list_display = ['Nombre','Stock']
    
    
admin.site.register(Productos,ProductosAdmin)
admin.site.register(Categorias)
admin.site.register(ProductosCategorias)
admin.site.register(Proveedores)
admin.site.register(Movimientos)
admin.site.register(DetallesMovimientoProducto)
    
     
    
    
    
    