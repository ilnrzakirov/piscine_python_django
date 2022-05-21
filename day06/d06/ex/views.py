from django.shortcuts import render
from django.conf import settings
from random import choice


def get_username(request):
    response = render(request, 'intro.html')
    if not request.COOKIES.get('user'):
        user = choice(settings.NAMES)
        request.COOKIES['user'] = user
        response = render(request, 'intro.html')
        response.set_cookie('user', user, max_age=42)
    return response
