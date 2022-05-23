from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.conf import settings
from random import choice
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from .models import Tip, UpVoice, DownVoice

from .forms import RegisterForm, TipForm


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
    success_url = 'home'


class LogoutView(LogoutView):
    next_page = 'home'


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


class TipView(ListView):
    template_name = 'index.html'
    context_object_name = 'tips'
    queryset = Tip.objects.all()

    def get(self, request, *args, **kwargs):
        if not request.COOKIES.get('user'):
            form = TipForm()
            data = Tip.objects.all()
            for tip in data:
                tip.upCount()
                tip.downCount()
            data = Tip.objects.all()
            user = choice(settings.NAMES)
            request.COOKIES['user'] = user
            response = render(request, 'index.html', context={'data': data, 'form': form})
            response.set_cookie('user', user, max_age=42)
            return response
        form = TipForm()
        data = Tip.objects.all()
        for tip in data:
            tip.upCount()
            tip.downCount()
        data = Tip.objects.all()
        return render(request, 'index.html', context={'data': data, 'form': form})

    def post(self, request, *args, **kwargs):
        flag = True
        if 'up' in request.POST:
            tip = Tip.objects.filter(id=request.POST['id'])
            allDownVote = tip[0].downVoice.all()
            for v in allDownVote:
                if v.user.username == request.user.username:
                    v.delete()
            allVote = tip[0].upVoice.all()
            for v in allVote:
                if v.user.username == request.user.username:
                    v.delete()
                    flag = False
            if flag:
                vote = UpVoice.objects.create(user=request.user)
                vote.save()
                Tip.objects.filter(id=request.POST['id'])[0].upVoice.add(vote)
            return redirect('home')

        if 'down' in request.POST:
            flag = True
            tip = Tip.objects.filter(id=request.POST['id'])
            allUpVote = tip[0].upVoice.all()
            for v in allUpVote:
                if v.user.username == request.user.username:
                    v.delete()
            allVote = tip[0].downVoice.all()
            for v in allVote:
                if v.user.username == request.user.username:
                    v.delete()
                    flag = False
            if flag:
                vote = DownVoice.objects.create(user=request.user)
                vote.save()
                Tip.objects.filter(id=request.POST['id'])[0].downVoice.add(vote)
            return redirect('home')

        if 'remove' in request.POST:
            tip = Tip.objects.filter(id=request.POST['id'])
            tip.delete()
            return redirect('home')

        form = TipForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            Tip.objects.create(author=user, content=form.cleaned_data['content'])
        data = Tip.objects.all()
        form = TipForm()
        return render(request, 'index.html', context={'data': data, 'form': form})


