from django.urls import path
from . import views 

urlpatterns = [
    path('ex02/', views.ex02, name='ex02'),
]
