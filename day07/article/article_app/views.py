from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
from random import choice
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from .models import Article


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