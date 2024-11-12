from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat'),
    path('chat/create/', views.create_chatroom, name='create_chatroom'),
    path('<str:room_name>/', views.chat_room, name='chat_room'),
]
