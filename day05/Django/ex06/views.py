from django.shortcuts import render, redirect
import psycopg2
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.views import View
from  .forms import UpdateForm

def db_init_view(request):
    try:
        db = settings.DATABASES['default']
        connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                                   host=db['HOST'], port=db['PORT'])
        with connect.cursor() as db_connect:
            # db_connect.execute("drop table if exists ex06_movies;")
            db_connect.execute("CREATE TABLE IF NOT EXISTS ex06_movies (episode_nb INT PRIMARY KEY, "
                               "title VARCHAR(64) UNIQUE NOT NULL, opening_crawl TEXT, director VARCHAR(32) NOT NULL, "
                               "producer VARCHAR(128) NOT NULL, release_date DATE NOT NULL, "
                               "created TIMESTAMP NOT NULL DEFAULT NOW(), updated TIMESTAMP NOT NULL DEFAULT NOW());")
            connect.commit()
            db_connect.execute("""
                        CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
            NEW.updated = now();
            NEW.created = OLD.created;
            RETURN NEW;
            END;
            $$ language 'plpgsql';
            CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
            ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
            update_changetimestamp_column();
            """)
            connect.commit()
            connect.close()
            return HttpResponse("Ok")
    except Exception as error:
        return HttpResponse(error)


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
    try:
        db = settings.DATABASES['default']
        connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                                   host=db['HOST'], port=db['PORT'])
        with connect.cursor() as db_connect:
            for mov in movList:
                db_connect.execute(f"SELECT title FROM ex06_movies WHERE episode_nb='{mov['episode_nb']}';")
                connect.commit()
                if db_connect.fetchone():
                    count += " Nok"
                    continue
                db_connect.execute(f"INSERT INTO ex06_movies (episode_nb, title, director, producer, "
                                   f"release_date) VALUES ({mov['episode_nb']}, '{mov['title']}', '{mov['director']}', "
                                   f"'{mov['producer']}', '{mov['release_date']}');")
                count += " Ok"
                connect.commit()
            connect.close()
            if not "Ok" in count:
                return HttpResponse("nothing to add")
            return HttpResponse(count)
    except Exception as error:
        return HttpResponse(error)


def display_view(request):
    try:
        db = settings.DATABASES['default']
        connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                                   host=db['HOST'], port=db['PORT'])
        with connect.cursor() as db_connect:
            db_connect.execute("SELECT * FROM ex06_movies;")
            if (db_connect.fetchone() == None):
                return HttpResponse("No data available")
            db_connect.execute("SELECT * FROM ex06_movies;")
            data = db_connect.fetchall()
            connect.close()
    except Exception as error:
        return HttpResponse(error)
    return render(request, 'display.html', context={'data': data})

class UpdateView(View):

    def get(self, request):
        try:
            db = settings.DATABASES['default']
            connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                                       host=db['HOST'], port=db['PORT'])
            with connect.cursor() as db_connect:
                db_connect.execute("SELECT * FROM ex06_movies;")
                if (db_connect.fetchone() == None):
                    return HttpResponse("No data available")
                db_connect.execute("SELECT * FROM ex06_movies;")
                data = db_connect.fetchall()
                connect.close()
                context = {'form': UpdateForm(choices=((line[1], line[1]) for line in data))}
                return render(request, 'ex06/update.html', context=context)
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
                db_connect.execute("SELECT * FROM ex06_movies;")
                if (db_connect.fetchone() == None):
                    return HttpResponse("No data available")
                db_connect.execute("SELECT * FROM ex06_movies;")
                data = db_connect.fetchall()
                choices = ((line[1], line[1]) for line in data)
        except Exception as error:
            print(error)
        context = UpdateForm(choices, request.POST)
        if context.is_valid():
            try:
                with connect.cursor() as db_connect:
                    db_connect.execute(f"UPDATE ex06_movies SET opening_crawl='{context.cleaned_data['opening_crawl']}'"
                                       f"WHERE title='{context.cleaned_data['title']}';")
                    connect.commit()
                    connect.close()
            except Exception as error:
                print(error)
        return redirect('update1')


