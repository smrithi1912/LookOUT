from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('search', views.results, name="search"),
    
]
