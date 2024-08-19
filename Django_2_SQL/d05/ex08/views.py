from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import psycopg2

def ex08(request):
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
            CREATE TABLE IF NOT EXISTS ex08_planets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate VARCHAR(64),
                diameter INT,
                orbital_period INT,
                population BIGINT,
                rotation_period INT,
                surface_water FLOAT,
                terrain VARCHAR(128)
            );
            CREATE TABLE IF NOT EXISTS ex08_people (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INT,
                mass REAL,
                homeworld VARCHAR(64) REFERENCES ex08_planets(name)
            );
        """
        cur.execute(create_table)
        connect.commit()
        cur.close()
        connect.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

def populate(request):
    connect = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )
    planets = []
    people = []
    with open('./ex08/planets.csv', 'r') as f:
        for line in f:
            data = line.strip().split('\t')
            if len(data) == 8:
                planets.append({
                    'name': data[0],
                    'climate': data[1] if data[1] != 'NULL' else None,
                    'diameter': int(data[2]) if data[2] != 'NULL' else None,
                    'orbital_period': int(data[3]) if data[3] != 'NULL' else None,
                    'population': int(data[4]) if data[4] != 'NULL' else None,
                    'rotation_period': int(data[5]) if data[5] != 'NULL' else None,
                    'surface_water': float(data[6]) if data[6] != 'NULL' else None,
                    'terrain': data[7] if data[7] != 'NULL' else None
                })
    with open('./ex08/people.csv', 'r') as f:
        for line in f:
            data = line.strip().split('\t')
            if len(data) == 8:
                people.append({
                    'name': data[0],
                    'birth_year': data[1] if data[1] != 'NULL' else None,
                    'gender': data[2] if data[2] != 'NULL' else None,
                    'eye_color': data[3] if data[3] != 'NULL' else None,
                    'hair_color': data[4] if data[4] != 'NULL' else None,
                    'height': int(data[5]) if data[5] != 'NULL' else None,
                    'mass': float(data[6]) if data[6] != 'NULL' else None,
                    'homeworld': data[7] if data[7] != 'NULL' else None
                })
    INSERT_PLANET = """
        INSERT INTO ex08_planets (name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    INSERT_PEOPLE = """
        INSERT INTO ex08_people (name, birth_year, gender, eye_color, hair_color, height, mass, homeworld)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    res = []
    try:
        cur = connect.cursor()
        for planet in planets:
            try:
                cur.execute(INSERT_PLANET, (
                    planet['name'],
                    planet['climate'],
                    planet['diameter'],
                    planet['orbital_period'],
                    planet['population'],
                    planet['rotation_period'],
                    planet['surface_water'],
                    planet['terrain']
                ))
                res.append(f"Planet inserted: {planet['name']}")
            except psycopg2.DatabaseError as e:
                connect.rollback()
                res.append(f"Error inserting planet {planet['name']}: {e}")
        for person in people:
            try:
                cur.execute(INSERT_PEOPLE, (
                    person['name'],
                    person['birth_year'],
                    person['gender'],
                    person['eye_color'],
                    person['hair_color'],
                    person['height'],
                    person['mass'],
                    person['homeworld']
                ))
                res.append(f"Person inserted: {person['name']}")
            except psycopg2.DatabaseError as e:
                connect.rollback()
                res.append(f"Error inserting person {person['name']}: {e}")
        connect.commit()
        cur.close()
        connect.close()
        res.append("OK")
        return HttpResponse("<br>".join(res))
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
        cur = connect.cursor()
        cur.execute("SELECT * FROM ex08_planets")
        res_planets = cur.fetchall()
        cur.execute("SELECT * FROM ex08_people")
        res_people = cur.fetchall()
        cur.close()
        connect.close()
        return render(request, 'ex08/display.html', {'planets': res_planets, 'people': res_people})
    except Exception as e:
        return HttpResponse(f"Error: {e}")
