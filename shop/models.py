from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Proveedores(models.Model):
    IdProveedor = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)  
    Direccion = models.CharField(max_length=100)                
    Telefono = models.CharField(max_length=20)
    Email = models.CharField(max_length=150)
    
class Productos(models.Model):
    IdProducto = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField()
    PrecioUnitario = models.DecimalField(max_digits=20, decimal_places=2)
    Stock = models.BigIntegerField()
    IdProveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

class Categorias(models.Model):
    IdCategoria = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField()  
    Productos = models.ManyToManyField(Productos, through='ProductosCategorias') 
    
    def __str__(self) -> str:
        return self.Nombre

class ProductosCategorias(models.Model):
    IdProducto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    IdCategoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    

