from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat'),
    path('<str:room_name>/', views.chat_room, name='chat_room'),
    path('create/', views.create_chatroom, name='create_chatroom'),
]
