from django.contrib import admin
from django.urls import path, include
from Register import views
urlpatterns = [
    path('register/', views.show),
    path('showall/', views.showall),
    path('showall/detail',views.showdetail)
]
