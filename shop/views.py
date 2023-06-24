from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.template import loader
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,UpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView,GenericAPIView
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import *
from  rest_framework import viewsets 
# Create your views here.

    
    
class UserListView(ListView):
    model = User
    template_name = "Users/user_list.html"
    context_object_name = 'object_list'

@permission_classes((AllowAny, ))
class ProductosApiView(viewsets.ModelViewSet):
    serializer_class = ProductosSerializer
    queryset = Productos.objects.all()
    
    def get_queryset(self):
        categoriaid = self.request.query_params.get('categoriaid')
        if categoriaid is not None:
            self.queryset = Productos.objects.filter(miscategorias__IdCategoria = categoriaid)
            return self.queryset
        return self.queryset

class CategoriasApiView(viewsets.ModelViewSet):
    serializer_class = CategoriasSerializer
    queryset = Categorias.objects.all()
    
class ProveedoresApiView(viewsets.ModelViewSet):
    serializer_class = ProveedoresSerializer
    queryset = Proveedores.objects.all()

class MovimientosApiView(viewsets.ModelViewSet):
    serializer_class = MovimientosSerializer
    queryset = Movimientos.objects.all()

class DetallesMovimientoProductoApiView(viewsets.ModelViewSet):
    serializer_class = DetallesMovimientoProductoSerializer
    queryset = DetallesMovimientoProducto.objects.all()