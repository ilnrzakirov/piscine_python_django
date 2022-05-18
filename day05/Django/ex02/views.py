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
            db_connect.execute("INSERT INTO ex02_movies (episode_nb, title, opening_crawl, director, producer, "
                               "release_date)")
            connect.commit()
            return HttpResponse("Ok")
    except Exception as error:
        return HttpResponse(error)


