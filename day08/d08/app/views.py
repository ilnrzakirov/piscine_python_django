from django.shortcuts import render
from django.views.generic import FormView, ListView
from .models import Image
from .forms import ImageForm


class IndexView(FormView, ListView):
    template_name = 'index.html'
    model = Image
    success_url = 'home'
    form_class = ImageForm
    context_object_name = 'data'
    queryset = Image.objects.all()
