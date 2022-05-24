from .models import Movies
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.shortcuts import redirect, render
from .forms import RemoveForm


def populate_view(request):
    movList = [
        {
            'episode_nb': 1,
            'title': 'The Phatom Menace',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '1999-05-19',
        }, {
            'episode_nb': 2,
            'title': 'Attack of th Clones',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2002-05-16',
        }, {
            'episode_nb': 3,
            'title': 'Revenge of the Sith',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2005-05-19',
        }, {
            'episode_nb': 4,
            'title': 'A New Hope',
            'director': 'George Lucas',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1977-05-25',
        }, {
            'episode_nb': 5,
            'title': 'The Empire Strikes Back',
            'director': 'Irvin Kershner',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1980-05-17',
        }, {
            'episode_nb': 6,
            'title': 'Return of the Jedi',
            'director': 'Richard Marquand',
            'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
            'release_date': '1983-05-25',
        }, {
            'episode_nb': 7,
            'title': 'The Force Awakens',
            'director': 'J.J. Abrams',
            'producer': 'Kathleen Kennedy, J.J. Abrams, Bryan Burk',
            'release_date': '2015-12-11',
        },
    ]
    count = ""
    for mov in movList:
        try:
            if Movies.objects.filter(episode_nb=mov['episode_nb']).count() == 0:
                Movies.objects.create(episode_nb=mov['episode_nb'], title=mov['title'], director=mov['director'],
                                      producer=mov['producer'], release_date=mov['release_date'])
                count += " Ok"
            else:
                count += " Nok"
        except Exception as error:
            return HttpResponse(error)
    if not "Ok" in count:
        return HttpResponse("nothing to add")
    return HttpResponse(count)


class DisplayView(ListView):
    template_name = 'ex05/display.html'
    context_object_name = 'data'
    queryset = Movies.objects.all()


class RemoveView(View):
    template_name = 'ex05/remove.html'

    def get(self, request):
        try:
            data = Movies.objects.all()
            if len(data) == 0:
                return HttpResponse("No data available")
            choices = ((line.title, line.title) for line in data)
            return render(request, 'ex05/remove.html', context={'form': RemoveForm(choices)})
        except Exception:
            return HttpResponse("No data available movies")

    def post(self, request):
        try:
            data = Movies.objects.all()
            if len(data) == 0:
                return redirect('remove')
        except Exception as error:
            return redirect('remove')
        choices = ((line.title, line.title) for line in data)
        context = RemoveForm(choices, request.POST)
        print(request.POST['title'])
        if context.is_valid():
            try:
                Movies.objects.filter(title=context.cleaned_data['title']).delete()
            except Exception as error:
                print(error)
        return redirect('remove')
