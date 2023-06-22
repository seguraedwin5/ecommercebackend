from django.urls import path, re_path,include
from shop.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView 

router = routers.DefaultRouter()
router.register('productos', ProductosApiView, 'productos')
router.register('categorias', CategoriasApiView, 'categorias')
router.register('proveedores', ProveedoresApiView, 'proveedores')
router.register('movimientos' , MovimientosApiView, 'movimientos')
router.register('detallesmovimientoproducto', DetallesMovimientoProductoApiView, 'detallesmovimientoproducto')

app_name = 'shop'

urlpatterns = [
    path("listview/", UserListView.as_view(), name="list_view"),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='tokenrefresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='tokenverify')
]
