from django.db import models
from django.contrib.auth.models import User
import datetime 
# Create your models here.

class Proveedores(models.Model):
    IdProveedor = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)  
    Direccion = models.CharField(max_length=100)                
    Telefono = models.CharField(max_length=20)
    Email = models.CharField(max_length=150)
    
class Productos(models.Model):
    IdProducto = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField()
    PrecioUnitario = models.DecimalField(max_digits=20, decimal_places=2)
    Stock = models.BigIntegerField()
    IdProveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    

class Categorias(models.Model):
    IdCategoria = models.AutoField(primary_key=True, verbose_name='idc')
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField()  
    productos = models.ManyToManyField(Productos, through='ProductosCategorias',related_name='miscategorias') 
    
    def __str__(self) -> str:
        return self.Nombre

class ProductosCategorias(models.Model):
    IdProducto = models.ForeignKey(Productos, on_delete=models.CASCADE  )
    IdCategoria = models.ForeignKey(Categorias, on_delete=models.CASCADE  )

class Movimientos(models.Model):
    class Tipos(models.TextChoices):
        ENTRADA = 'E'
        SALIDA = 'S'
        
    IdMovimiento = models.AutoField(primary_key=True)
    Fecha = models.DateField(default=datetime.date.today())
    Tipo = models.CharField(max_length=20, choices=Tipos.choices)
    Descripcion = models.TextField()
    IdUsuario = models.ForeignKey(User, on_delete=models.CASCADE)

class DetallesMovimientoProducto(models.Model):
    IdDetalle = models.AutoField(primary_key=True)
    IdMovimiento = models.ForeignKey(Movimientos, on_delete=models.CASCADE)
    IdProducto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    Cantidad = models.BigIntegerField()
    PrecioTotal = models.DecimalField(max_digits=20, decimal_places=2)
    
