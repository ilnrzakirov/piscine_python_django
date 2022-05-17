from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from . import forms
from django.conf import settings


class SubmitView(FormView):
    form_class = forms.DataForm
    template_name = 'submit.html'
    success_url = 'submit.html'

    def post(self, request, *args, **kwargs):
        form = forms.DataForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("input_data")
            with open(settings.LOG_ROOT, "a") as file:
                file.write(text)
                file.write("\n")
        return redirect('submit')


def history_view(request):
    print(settings.LOG_ROOT)
    with open(settings.LOG_ROOT, "r") as file:
        res = []
        for line in file.readlines():
            res.append(line)
        return render(request, 'history.html', context={'text': res})
