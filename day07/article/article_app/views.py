from django.shortcuts import render, redirect
from .forms import RegisterForm, ArticleForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
from random import choice
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.views.generic import ListView, DetailView
from .models import Article, UserFavouriteArticle


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'login.html', context={'form': form})


class LoginView(LoginView):
    redirect_authenticated_user = 'home'
    template_name = 'login.html'
    success_url = 'home'


class LogoutView(LogoutView):
    next_page = 'home'


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'data'
    queryset = Article.objects.all()


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

    def post(self, request):
        if 'Favourites' in request.POST:
            article = Article.objects.get(id=request.POST['id'])
            userFav = UserFavouriteArticle.objects.filter(user=request.user)
            print(userFav)
            for favArtic in userFav:
                print(favArtic.article)
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

