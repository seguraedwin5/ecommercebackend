from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView
from django.template import loader
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,UpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView,GenericAPIView
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import AllowAny
from .serializers import ProductoSerializer
from .models import Producto
# Create your views here.
class StartView(TemplateView):
    template_name = 'inicio.html'
    
    
class UserListView(ListView):
    model = User
    template_name = "Users/user_list.html"
    context_object_name = 'object_list'

@permission_classes((AllowAny, ))
class ProductListApi(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
