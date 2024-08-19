from django.urls import path
from . import views 

urlpatterns = [
    path('ex02/init', views.ex02),
    path('ex02/populate', views.populate),
    path('ex02/display', views.display),
]
