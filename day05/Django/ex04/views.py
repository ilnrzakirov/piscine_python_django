from django.shortcuts import render, redirect
import psycopg2
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.views import View
from .forms import RemoveForm


# Create your views here.

def db_init_view(request):
    try:
        db = settings.DATABASES['default']
        connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                                   host=db['HOST'], port=db['PORT'])
        with connect.cursor() as db_connect:
            db_connect.execute("drop table if exists ex04_movies;")
            db_connect.execute("CREATE TABLE IF NOT EXISTS ex04_movies (episode_nb INT PRIMARY KEY, "
                               "title VARCHAR(64) UNIQUE NOT NULL, opening_crawl TEXT, director VARCHAR(32) NOT NULL, "
                               "producer VARCHAR(128) NOT NULL, release_date DATE NOT NULL);")
            connect.commit()
            connect.close()
            return HttpResponse("Ok")
    except Exception as error:
        return HttpResponse(error)


def populate_view(request):
    try:
        db = settings.DATABASES['default']
        connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                                   host=db['HOST'], port=db['PORT'])
        with connect.cursor() as db_connect:
            db_connect.execute("INSERT INTO ex04_movies (episode_nb, title, director, producer, "
                               "release_date) VALUES (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', "
                               "'1999-05-19'), (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', "
                               "'2002-05-16'), (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', "
                               "'2005-05-19'), (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', "
                               "'1977-05-25'), (5, 'The Empire Strikes Back', 'Irvin Kershner', "
                               "'Gary Kurtz, Rick McCallum', '1980-05-17'), (6, 'Return of the Jedi', "
                               "'Richard Marquand ', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),"
                               "(7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', "
                               "'2015-12-11');")
            connect.commit()
            connect.close()
            return HttpResponse("Ok")
    except Exception as error:
        return HttpResponse(error)


def display_view(request):
    try:
        db = settings.DATABASES['default']
        connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                                   host=db['HOST'], port=db['PORT'])
        with connect.cursor() as db_connect:
            db_connect.execute("SELECT * FROM ex04_movies;")
            if (db_connect.fetchone() == None):
                return HttpResponse("No data available")
            db_connect.execute("SELECT * FROM ex04_movies;")
            data = db_connect.fetchall()
            connect.close()
    except Exception as error:
        return HttpResponse(error)
    return render(request, 'display.html', context={'data': data})


class RemoveView(View):

        def get(self, request):
            try:
                db = settings.DATABASES['default']
                connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                                           host=db['HOST'], port=db['PORT'])
                with connect.cursor() as db_connect:
                    db_connect.execute("SELECT * FROM ex04_movies;")
                    if (db_connect.fetchone() == None):
                        return HttpResponse("No data available")
                    db_connect.execute("SELECT * FROM ex04_movies;")
                    data = db_connect.fetchall()
                    connect.close()
                    context = {'form': RemoveForm(choices=((line[1], line[1]) for line in data))}
                    return render(request, 'remove.html', context=context)
            except Exception as error:
                print(error)
                return HttpResponse("No data available")

        def post(self, request):
            global connect
            try:
                db = settings.DATABASES['default']
                connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                                           host=db['HOST'], port=db['PORT'])
                with connect.cursor() as db_connect:
                    db_connect.execute("SELECT title FROM ex04_movies;")
                    data = db_connect.fetchall()
                    choices = ((line[0], line[0]) for line in data)
            except Exception as error:
                HttpResponse("No data available")
            context = RemoveForm(choices, request.POST)
            if context.is_valid():
                try:
                    with connect.cursor() as db_connect:
                        db_connect.execute(f"DELETE FROM ex04_movies WHERE title='{context.cleaned_data['title']}';")
                        connect.commit()
                except Exception as error:
                    print(error)
            return redirect('remove')
