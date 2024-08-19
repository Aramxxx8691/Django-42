import json
from django.shortcuts import render
from django.conf import settings
from .models import People, Movies, Planets
from .forms import SearchForm

def ex10(request):
    json_file_path = settings.BASE_DIR / 'ex10' / 'ex10_initial_data.json'
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    movie_data = [item for item in data if item['model'] == 'ex10.movies']
    planet_data = [item for item in data if item['model'] == 'ex10.planets']
    people_data = [item for item in data if item['model'] == 'ex10.people']

    Planets.objects.all().delete()
    People.objects.all().delete()
    Movies.objects.all().delete()

    planet_instances = {}
    for planet in planet_data:
        planet_instance = Planets.objects.create(id=planet['pk'], **planet['fields'])
        planet_instances[planet['pk']] = planet_instance
    
    for person in people_data:
        homeworld_id = person['fields'].pop('homeworld', None)
        if homeworld_id:
            homeworld = planet_instances.get(homeworld_id)
            if homeworld:
                People.objects.create(id=person['pk'], homeworld=homeworld, **person['fields'])
            else:
                print(f"Warning: Planet with ID '{homeworld_id}' does not exist.")
        else:
            People.objects.create(id=person['pk'], **person['fields'])
    
    for movie in movie_data:
        character_ids = movie['fields'].pop('characters', [])
        movie_instance = Movies.objects.create(id=movie['pk'], **movie['fields'])
        characters = People.objects.filter(id__in=character_ids)
        if characters.exists():
            movie_instance.characters.set(characters)
        else:
            print(f"Warning: No characters found for movie '{movie_instance.title}'.")
    
    form = SearchForm(request.GET or None)
    results = []

    if form.is_valid():
        min_release_date = form.cleaned_data['min_release_date']
        max_release_date = form.cleaned_data['max_release_date']
        min_planet_diameter = form.cleaned_data['min_planet_diameter']
        character_gender = form.cleaned_data['character_gender']
        
        # Filtering based on form input
        characters = People.objects.filter(gender=character_gender)
        movies = Movies.objects.filter(release_date__range=[min_release_date, max_release_date])
        planets = Planets.objects.filter(diameter__gte=min_planet_diameter)
        
        for character in characters:
            for movie in movies:
                if movie.characters.filter(id=character.id).exists():
                    homeworld = character.homeworld
                    if homeworld and homeworld in planets:
                        results.append({
                            'character_name': character.name,
                            'character_gender': character.gender,
                            'movie_title': movie.title,
                            'homeworld_name': homeworld.name,
                            'homeworld_diameter': homeworld.diameter
                        })
    return render(request, 'ex10/display.html', {
        'form': form,
        'results': results
    })
