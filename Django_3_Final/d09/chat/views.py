from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from .models import Chatroom, Message
from django.http import HttpResponseRedirect
from django.urls import reverse

class ChatHomeView(LoginRequiredMixin, View):
    def get(self, request):
        chatrooms = Chatroom.objects.all()
        return render(request, 'chat/chat_home.html', {
            'chatrooms': chatrooms,
            'username': request.user.username
        })

    def post(self, request):
        name = request.POST.get('name')
        if name:
            Chatroom.objects.create(name=name)
        return HttpResponseRedirect(reverse('chat'))

class ChatRoomView(LoginRequiredMixin, View):
    def get(self, request, room_name):
        chatroom = get_object_or_404(Chatroom, name=room_name)
        chatroom.users.add(request.user)
        chatroom.save()
        messages = Message.objects.filter(chatroom=chatroom).order_by('-timestamp')[:3]
        messages = messages[::-1]
        users = chatroom.users.all()
        return render(request, 'chat/chat_room.html', {
            'room_name': chatroom.name,
            'username': request.user.username,
            'messages': messages,
            'users': users
        })

class CreateChatroomView(LoginRequiredMixin, View):
    def post(self, request):
        room_name = request.POST.get('name')
        if ' ' in room_name:
            messages.error(request, "Room name cannot contain spaces.")
            return HttpResponseRedirect(reverse('chat'))
        if Chatroom.objects.filter(name=room_name).exists():
            messages.error(request, "A chatroom with that name already exists.")
            return HttpResponseRedirect(reverse('chat'))
        Chatroom.objects.create(name=room_name)
        return HttpResponseRedirect(reverse('chat_room', args=[room_name]))

class CheckAndEnterChatroomView(View):
    def get(self, request, room_name):
        chatroom, created = Chatroom.objects.get_or_create(name=room_name)
        return redirect('chat_room', room_name=chatroom.name)
