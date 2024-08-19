import json
from django.shortcuts import render
from django.conf import settings
from .models import Planets, People

def display(request):
    with open(settings.BASE_DIR / 'ex09/ex09_initial_data.json', 'r') as file:
        data = json.load(file)
    for entry in data:
        model_name = entry['model']
        fields = entry['fields']
        if model_name == 'ex09.planets':
            Planets.objects.update_or_create(id=entry['pk'], defaults=fields)
        elif model_name == 'ex09.people':
            homeworld_id = fields.pop('homeworld', None)
            homeworld = Planets.objects.get(id=homeworld_id) if homeworld_id else None
            fields['homeworld'] = homeworld
            People.objects.update_or_create(id=entry['pk'], defaults=fields)
    people = People.objects.select_related('homeworld').order_by('name')
    context = {'people': people,}
    return render(request, 'ex09/display.html', context)
