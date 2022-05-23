from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('populate/', views.populate_view),
    path('init/', views.db_init_view),
    path('display/', views.display_view),
    path('update/', views.UpdateView.as_view(), name='update1'),
]
