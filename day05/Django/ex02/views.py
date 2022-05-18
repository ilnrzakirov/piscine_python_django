from django.shortcuts import render
import psycopg2
from django.conf import settings
from django.http import HttpRequest, HttpResponse


# Create your views here.

def db_init_view(request):
    try:
        db = settings.DATABASES['default']
        connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                                   host=db['HOST'], port=db['PORT'])
        with connect.cursor() as db_connect:
            db_connect.execute("drop table if exists ex02_movies;")
            db_connect.execute("CREATE TABLE IF NOT EXISTS ex02_movies (episode_nb INT PRIMARY KEY, "
                               "title VARCHAR(64) UNIQUE NOT NULL, opening_crawl TEXT, director VARCHAR(32) NOT NULL, "
                               "producer VARCHAR(128) NOT NULL, release_date DATE NOT NULL);")
            connect.commit()
            return HttpResponse("Ok")
    except Exception as error:
        return HttpResponse(error)


def populate_view(request):
    try:
        db = settings.DATABASES['default']
        connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                                   host=db['HOST'], port=db['PORT'])
        with connect.cursor() as db_connect:
            db_connect.execute("INSERT INTO ex02_movies (episode_nb, title, director, producer, "
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
            db_connect.execute("SELECT * FROM ex02_movies;")
            if (db_connect.fetchone() == None):
                return HttpResponse("No data available")
            data = db_connect.fetchall()
            connect.close()
    except Exception as error:
        return HttpResponse(error)
    return render(request, 'display.html', context={'data': data})
