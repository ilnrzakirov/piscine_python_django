from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_username, name='intro'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.register_view, name='register')
]