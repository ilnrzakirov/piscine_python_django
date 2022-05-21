from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SubmitView.as_view(), name='submit'),
    path('history/', views.history_view),
]
