from django.shortcuts import render


def django_view(request):
    return render(request, 'ex01/django.html')


def display_view(request):
    return render(request, 'ex01/display.html')


def templates_view(request):
    return render(request, 'ex01/templates.html')
