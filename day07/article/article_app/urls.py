from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', views.IndexView.as_view(), name='home'),
    path('article/', views.IndexView.as_view()),
]