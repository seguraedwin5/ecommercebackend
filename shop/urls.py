from django.urls import path
from shop.views import UserListView

urlpatterns = [
    path("listview/", UserListView.as_view(), name="list_view")
]
