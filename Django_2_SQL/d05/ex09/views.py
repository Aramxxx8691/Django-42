from django.shortcuts import render
from .models import People

def display(request):
    people = People.objects.select_related('homeworld').order_by('name')
    context = {'people': people}
    return render(request, 'ex09/display.html', context)
