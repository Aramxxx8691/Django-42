from django.shortcuts import get_object_or_404, render
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
        messages = Message.objects.filter(chatroom=chatroom).order_by('timestamp')
        return render(request, 'chat/chat_room.html', {
            'room_name': chatroom.name,
            'username': request.user.username,
            'messages': messages
        })

class CreateChatroomView(LoginRequiredMixin, View):
    def post(self, request):
        room_name = request.POST.get('name')
        if Chatroom.objects.filter(name=room_name).exists():
            messages.error(request, "A chatroom with that name already exists.")
            return HttpResponseRedirect(reverse('chat'))
        Chatroom.objects.create(name=room_name)
        return HttpResponseRedirect(reverse('chat_room', args=[room_name]))
