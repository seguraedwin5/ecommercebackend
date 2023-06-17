from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.template import loader
# Create your views here.
class UserListView(ListView):
    model = User
    template_name = "Users/user_list.html"
    context_object_name = 'object_list'