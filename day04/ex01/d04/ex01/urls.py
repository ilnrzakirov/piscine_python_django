from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('ex01/django', views.django_view),
    path('ex01/display', views.display_view),
    path('ex01/templates', views.templates_view),
]