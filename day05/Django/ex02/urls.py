from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('init/', views.db_init_view),
    path('populate/', views.populate_view)
]
