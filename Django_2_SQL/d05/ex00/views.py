
from django.http import HttpResponse
from django.conf import settings

import psycopg2

def ex00(request):
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
            CREATE TABLE IF NOT EXISTS ex00_movies (
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