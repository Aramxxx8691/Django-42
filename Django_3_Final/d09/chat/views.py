# chat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Chatroom, Message

@login_required
def chat_home(request):
    chatrooms = Chatroom.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Chatroom.objects.create(name=name)
        return redirect('chat_home')
    
    return render(request, 'chat/chat_home.html', {'chatrooms': chatrooms})

@login_required
def chat_room(request, room_name):
    chatroom = get_object_or_404(Chatroom, name=room_name)
    return render(request, 'chat/chat_room.html', {'room_name': chatroom.name})


@login_required
def create_chatroom(request):
    if request.method == 'POST':
        room_name = request.POST['name']
        if Chatroom.objects.filter(name=room_name).exists():
            messages.error(request, "A chatroom with that name already exists.")
            return redirect('chat')
        chatroom = Chatroom.objects.create(name=room_name)
        return redirect('chat_room', room_name=chatroom.name)
    return redirect('chat')
