from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatHomeView.as_view(), name='chat'),
    path('chat/create/', views.CreateChatroomView.as_view(), name='create_chatroom'),
    path('<str:room_name>/', views.ChatRoomView.as_view(), name='chat_room'),
    path('<str:room_name>/check/', views.CheckAndEnterChatroomView.as_view(), name='check'),
]
