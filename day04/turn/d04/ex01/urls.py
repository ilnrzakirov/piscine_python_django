from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('django/', views.django_view, name='django'),
    path('display/', views.display_view, name='display'),
    path('templates/', views.templates_view, name='templates'),
]