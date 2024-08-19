from django.urls import path
from . import views 

urlpatterns = [
    path('ex08/init', views.ex08),
    path('ex08/populate', views.populate),
    path('ex08/display', views.display),
]
