from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.RegistrationWithCreateView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', views.IndexView.as_view(), name='home'),
    path('article/', views.IndexView.as_view(), name='article'),
    path('add/', views.AddArticleWithCreateView.as_view(), name='add_article'),
    path('publications/', views.PublicationsView.as_view(), name='public'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
    path('accounts/profile/', views.PublicationsView.as_view()),
    path('favourites/', views.MyArticleView.as_view(), name='fav'),
    path('add_fav/', views.AddArticleFromFavorites.as_view(), name='add_fav'),
    path('last_public/', views.LastArticleView.as_view(), name='last_public'),
]