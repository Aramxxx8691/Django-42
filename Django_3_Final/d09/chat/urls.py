from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatHomeView.as_view(), name='chat'),
    path('chat/create/', views.CreateChatroomView.as_view(), name='create_chatroom'),  # Create chatroom view
    path('<str:room_name>/', views.ChatRoomView.as_view(), name='chat_room'),  # Specific chatroom view
]
