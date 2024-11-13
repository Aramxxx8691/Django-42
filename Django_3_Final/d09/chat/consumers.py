import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the room name from the URL route
        self.room_name = self.scope['url_route']['kwargs'].get('room_name')
        self.room_group_name = f'chat_{self.room_name}' if self.room_name else 'chat_global'  # Default to global chat if no room name
        # Get the username of the user joining the chat
        self.user = self.scope["user"].username
        # Join the room group (either private chat or global chat)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # Notify other users (excluding the joining user) that a new user has joined
        if self.room_name:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_join_message',
                    'user': self.user  # Include the joining user's name for private chat
                }
            )
        else:
            # In the case of the global chat, notify everyone that a user has joined
            await self.channel_layer.group_send(
                'chat_global',
                {
                    'type': 'chat_join_message',
                    'user': self.user  # Include the joining user's name for global chat
                }
            )
        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Notify all users (excluding the leaving user) that a user has left
        if self.room_name:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_leave_message',
                    'user': self.user  # Include the leaving user's name
                }
            )
        else:
            # Global chat leaving message
            await self.channel_layer.group_send(
                'chat_global',
                {
                    'type': 'chat_leave_message',
                    'user': self.user  # Include the leaving user's name
                }
            )
        # Leave the room group when the user disconnects
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive a message from WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')
        # Send the received message to the correct group (private or global chat)
        if self.room_name:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'user': self.user,
                    'message_type': 'user_message'
                }
            )
        else:
            await self.channel_layer.group_send(
                'chat_global',
                {
                    'type': 'chat_message',
                    'message': message,
                    'user': self.user,
                    'message_type': 'user_message'
                }
            )

    async def chat_join_message(self, event):
        # Handle the event when a user joins the chat
        if event["user"] == self.user:
            # If it's the current user, send a personal join message
            await self.send(text_data=json.dumps({
                'message': f'You have joined the chat',
                'user': 'Server',
                'message_type': 'join_message'
            }))
        else:
            # Send a join message to other users in the chat
            await self.send(text_data=json.dumps({
                'message': f'{event["user"]} has joined the chat',
                'user': 'Server',
                'message_type': 'join_message'
            }))

    async def chat_leave_message(self, event):
        # Handle the event when a user leaves the chat
        if event["user"] != self.user:
            await self.send(text_data=json.dumps({
                'message': f'{event["user"]} has left the chat',
                'user': 'Server',
                'message_type': 'leave_message'
            }))

    async def chat_message(self, event):
        # Handle regular chat messages
        message = event['message']
        user = event['user']
        message_type = event['message_type']

        # Send the message to the WebSocket client
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'message_type': message_type
        }))
