from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.conf import settings
from random import choice
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm


def get_username(request):
    response = render(request, 'intro.html')
    if not request.COOKIES.get('user'):
        user = choice(settings.NAMES)
        request.COOKIES['user'] = user
        response = render(request, 'intro.html')
        response.set_cookie('user', user, max_age=42)
    return response


class LoginView(LoginView):
    redirect_authenticated_user = 'intro'
    template_name = 'login.html'
    success_url = 'intro'


class LogoutView(LogoutView):
    next_page = 'intro'


def register_view(request):
    if request.user.is_authenticated:
        return redirect('intro')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('intro')
    else:
        form = RegisterForm()
    return render(request, 'login.html', context={'form': form})
