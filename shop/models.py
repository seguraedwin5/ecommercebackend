from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Producto(models.Model):
    Id = models.IntegerField(primary_key=True, max_length= 50)
    Nombre = models.CharField(max_length=50)
    Cantidad = models.IntegerField(max_length=50)
    
    def __str__(self) -> str:
        return self.Nombre

class Categoria(models.Model):
    Id = models.IntegerField(primary_key=True, max_length=50)
    Nombre = models.CharField(max_length=50)
    
class ProductoxCategoria(models.Model):
    IdProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    IdCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
class DetallesProducto(models.Model):
    Precio = models.PositiveIntegerField()
    Imagen = models.FileField()
    Descripcion = models.CharField(max_length=50)
    Opiniones = models.TextField()
    
class CarroCompras(models.Model):
    IdProducto = models.ForeignKey(Producto, on_delete=models.deletion.CASCADE)