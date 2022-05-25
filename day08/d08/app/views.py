from django.views.generic import FormView, ListView
from .models import Image
from .forms import ImageForm
from django.urls import reverse_lazy


class IndexView(FormView, ListView):
    template_name = 'index.html'
    model = Image
    success_url = reverse_lazy('home')
    form_class = ImageForm
    context_object_name = 'data'
    queryset = Image.objects.all()

    def form_valid(self, form: ImageForm):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form: ImageForm):
        return super().form_invalid(form)
