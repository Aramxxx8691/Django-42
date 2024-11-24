from .models import Chatroom, Message
from django.contrib.auth.models import User
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs'].get('room_name')
        if not self.room_name:
            await self.close()
            return
        self.room_group_name = f'chat_{self.room_name}'
        self.user = self.scope["user"].username
        # Fetch or create the Chatroom instance
        self.chatroom = await database_sync_to_async(Chatroom.objects.get)(name=self.room_name)
        user_instance = await database_sync_to_async(User.objects.get)(username=self.user)
        # Add the current user to the chatroom
        await database_sync_to_async(self.chatroom.users.add)(user_instance)
        # Join the group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # Notify all clients of the new user
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_join_message',
                'user': self.user
            }
        )
        # Notify all clients to update the user list
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'update_user_list',
                'users': await self.get_usernames()
            }
        )
        await self.accept()

    async def disconnect(self, close_code):
        if self.room_name:
            user_instance = await database_sync_to_async(User.objects.get)(username=self.user)
            # Remove the user from the chatroom
            await database_sync_to_async(self.chatroom.users.remove)(user_instance)
            # Notify all clients of the user's departure
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_leave_message',
                    'user': self.user
                }
            )
            # Notify all clients to update the user list
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'update_user_list',
                    'users': await self.get_usernames()
                }
            )
            # Leave the group
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')
        # Fetch the Chatroom and User instances
        chatroom = await database_sync_to_async(Chatroom.objects.get)(name=self.room_name)
        user = await database_sync_to_async(User.objects.get)(username=self.user)
        # Save the message
        await database_sync_to_async(Message.objects.create)(
            chatroom=chatroom,
            user=user,
            content=message
        )
        # Broadcast the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user,
                'message_type': 'user_message'
            }
        )

    async def chat_join_message(self, event):
        if event["user"] == self.user:
            await self.send(text_data=json.dumps({
                'message': f'You have joined the chat',
                'user': 'Server',
                'message_type': 'join_message'
            }))
        else:
            await self.send(text_data=json.dumps({
                'message': f'{event["user"]} has joined the chat',
                'user': 'Server',
                'message_type': 'join_message'
            }))

    async def chat_leave_message(self, event):
        if event["user"] != self.user:
            await self.send(text_data=json.dumps({
                'message': f'{event["user"]} has left the chat',
                'user': 'Server',
                'message_type': 'leave_message'
            }))

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        message_type = event['message_type']
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'message_type': message_type
        }))

    async def update_user_list(self, event):
        # Send the updated user list to WebSocket
        await self.send(text_data=json.dumps({
            'message_type': 'user_list_update',
            'users': event['users']
        }))

    @database_sync_to_async
    def get_usernames(self):
        # Get a list of usernames in the chatroom
        return list(self.chatroom.users.values_list('username', flat=True))
