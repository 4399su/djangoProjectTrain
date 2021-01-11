from django.contrib import admin
from django.urls import path, include
from showMovie import views
urlpatterns = [
    path('', views.showMovie)
]
