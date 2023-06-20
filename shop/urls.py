from django.urls import path, re_path
from shop.views import UserListView, ProductListApi
app_name = 'shop'

urlpatterns = [
    path("listview/", UserListView.as_view(), name="list_view"),
    path(r'api/getproducts', ProductListApi.as_view(), name="getproducts"),
]
