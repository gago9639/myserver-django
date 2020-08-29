from django.contrib import admin
from django.urls import include, path

from api import views

urlpatterns = [
    path('', views.index),
    path('api/login', views.login),
    path('api/register', views.register),
]
