from django.urls import path
from . import views 

urlpatterns = [
    path('ex10/', views.ex10, name='search_results'),
]
