from django.shortcuts import render, redirect
from .forms import RegisterForm, ArticleForm, AddForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
from random import choice
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.views.generic import ListView, DetailView, CreateView
from .models import Article, UserFavouriteArticle
from django.views.generic.edit import ModelFormMixin


class LoginView(LoginView):
    redirect_authenticated_user = 'home'
    template_name = 'login.html'
    success_url = 'home'


class LogoutView(LogoutView):
    next_page = 'home'


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'data'
    queryset = Article.objects.order_by('created')

    def post(self, request):
        if 'Favourites' in request.POST:
            article = Article.objects.get(id=request.POST['id'])
            userFav = UserFavouriteArticle.objects.filter(user=request.user)
            for favArtic in userFav:
                if favArtic.article.title == article.title:
                    return redirect('home')
            fav = UserFavouriteArticle.objects.create(user=request.user, article=article)
        return redirect('home')


class AddArticleView(FormView):
    template_name = 'add_article.html'
    form_class = ArticleForm

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            Article.objects.create(author=user, content=form.cleaned_data['content'], title=form.cleaned_data['title'],
                                   synopsis=form.cleaned_data['synopsis'])
        return redirect('home')


class PublicationsView(ListView):
    template_name = 'publications.html'
    context_object_name = 'data'
    queryset = Article.objects.all()

    def get_queryset(self):
        context = Article.objects.filter(author=self.request.user)
        return context


    def post(self, request):
        if 'Favourites' in request.POST:
            article = Article.objects.get(id=request.POST['id'])
            userFav = UserFavouriteArticle.objects.filter(user=request.user)
            for favArtic in userFav:
                if favArtic.article.title == article.title:
                    return redirect('public')
            fav = UserFavouriteArticle.objects.create(user=request.user, article=article)
        return redirect('public')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'data'
    queryset = Article.objects.all()


class MyArticleView(ListView):
    model = UserFavouriteArticle
    template_name = 'my_articles.html'
    context_object_name = 'data'

    def get_queryset(self):
        context = UserFavouriteArticle.objects.filter(user=self.request.user)
        return context


class RegistrationWithCreateView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')


class AddArticleWithCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'add_article.html'

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = ArticleForm(request.POST)
            if form.is_valid():
                user = User.objects.get(username=request.user.username)
                Article.objects.create(author=user, content=form.cleaned_data['content'],
                                       title=form.cleaned_data['title'],
                                       synopsis=form.cleaned_data['synopsis'])
            return redirect('home')


class AddArticleFromFavorites(CreateView):
    model = Article
    fields = ('title', 'author', 'synopsis', 'id')
    template_name = 'add_fav.html'
    context_object_name = 'data'

    def get_queryset(self):
        context = Article.objects.all()
        return context


class LastArticleView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'data'

    def get_queryset(self):
        context = Article.objects.order_by('-id')[0:3]
        return context