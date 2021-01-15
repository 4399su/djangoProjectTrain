from django.contrib import admin
from django.urls import path, include
from Register import views
urlpatterns = [
    path('', views.show),
]
