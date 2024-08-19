
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import psycopg2

def ex04(request):
    try:
        connect = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cur = connect.cursor()
        create_table = """
            CREATE TABLE ex04_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb SERIAL PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );
        """
        cur.execute(create_table)
        connect.commit()
        cur.close()
        connect.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)

def populate(request):
    try:
        connect = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        movies = [
            {
                "episode_nb": 1,
                "title": "The Phantom Menace",
                "director": "George Lucas",
                "producer": "Rick McCallum",
                "release_date": "1999-05-19"
            },
            {
                "episode_nb": 2,
                "title": "Attack of the Clones",
                "director": "George Lucas",
                "producer": "Rick McCallum",
                "release_date": "2002-05-16"
            },
            {
                "episode_nb": 3,
                "title": "Revenge of the Sith",
                "director": "George Lucas",
                "producer": "Rick McCallum",
                "release_date": "2005-05-19"
            },
            {
                "episode_nb": 4,
                "title": "A New Hope",
                "director": "George Lucas",
                "producer": "Gary Kurtz, Rick McCallum",
                "release_date": "1977-05-25"
            },
            {
                "episode_nb": 5,
                "title": "The Empire Strikes Back",
                "director": "Irvin Kershner",
                "producer": "Gary Kutz, Rick McCallum",
                "release_date": "1980-05-17"
            },
            {
                "episode_nb": 6,
                "title": "Return of the Jedi",
                "director": "Richard Marquand",
                "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
                "release_date": "1983-05-25"
            },
            {
                "episode_nb": 7,
                "title": "The Force Awakens",
                "director": "J.J. Abrams",
                "producer": "Kathleen Kennedy, J.J. Abrams, Bryan Burk",
                "release_date": "2015-12-11"
            },
            {
                "episode_nb": 8,
                "title": "The Last Jedi",
                "director": "Rian Johnson",
                "producer": "Kathleen Kennedy, Ram Bergman",
                "release_date": "2017-12-13"
            },
            {
                "episode_nb": 9,
                "title": "The Rise of Skywalker",
                "director": "J.J. Abrams",
                "producer": "Kathleen Kennedy, J.J. Abrams, Michelle Rejwan",
                "release_date": "2019-12-18"
            },
        ]
        INSERT_DATA = """
            INSERT INTO ex04_movies (title, episode_nb, director, producer, release_date)
            VALUES (%s, %s, %s, %s, %s);
        """.format(tabel_name='ex04_movies')
        res = []
        with connect.cursor() as cur:
            for movie in movies:
                try:
                    cur.execute(INSERT_DATA, (movie['title'], movie['episode_nb'], movie['director'], movie['producer'], movie['release_date']))
                    res.append("OK")
                    connect.commit()
                except psycopg2.DatabaseError as e:
                    connect.rollback()
                    res.append(e)
        return HttpResponse("<br>".join(str(i) for i in res))
    except Exception as e:
        return HttpResponse(e)

def display(request):
    try:
        connect = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        with connect.cursor() as cur:
            cur.execute("SELECT * FROM ex04_movies")
            res = cur.fetchall()
        connect.close()
        return render(request, 'ex04/display.html', {'movies': res})
    except Exception as e:
        return HttpResponse(e)

def remove(request):
    try:
        connect = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        if request.method == 'POST':
            title = request.POST.get('title')
            if title:
                with connect.cursor() as cur:
                    cur.execute("DELETE FROM ex04_movies WHERE title = %s", [title])
                    connect.commit()
        with connect.cursor() as cur:
            cur.execute("SELECT title FROM ex04_movies")
            res = cur.fetchall()
        if not res:
            return HttpResponse("No data available")
        connect.close()
        return render(request, 'ex04/remove.html', {'movies': res})
    except Exception as e:
        return HttpResponse(str(e))
