from django.http import HttpResponse

# Create your views here.

def ex01(request):
    return HttpResponse("Movies model created!")