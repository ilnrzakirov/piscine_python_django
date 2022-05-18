from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('populate/', views.populate_view),
    path('display/', views.DisplayView.as_view()),
]
