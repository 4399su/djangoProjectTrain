from django.contrib import admin
from django.urls import path, include
from SQLtest import views

urlpatterns = [
    path('', views.showSQL)
]
