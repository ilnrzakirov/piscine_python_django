from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('ex01/django', views.django_view, name='django'),
    path('ex01/display', views.display_view, name='display'),
    path('ex01/templates', views.templates_view, name='templates'),
]