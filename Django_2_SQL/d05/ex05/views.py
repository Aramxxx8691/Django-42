from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

def populate(request):
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
    res = []
    for movie in movies:
        try:
            Movies.objects.create(**movie)
            res.append("OK")
        except Exception as e:
            res.append(str(e))
    return HttpResponse("<br>".join(res))

def display(request):
    movies = Movies.objects.all()
    if not movies:
        return HttpResponse("No data available")
    return render(request, 'ex03/display.html', {'movies': movies})

def remove(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Movies.objects.filter(title=title).delete()
    movies = Movies.objects.all()
    if not movies:
        return HttpResponse("No data available")
    return render(request, 'ex03/remove.html', {'movies': movies})