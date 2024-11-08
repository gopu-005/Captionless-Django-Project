from django.urls import path
from . import views

urlpattrens = [
    path("", views.home, name = "home"),
]