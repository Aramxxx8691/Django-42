import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the room name from the URL route
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        
        # Get the username of the user joining the chat
        self.user = self.scope["user"].username

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Notify all users (excluding the joining user) that a new user has joined
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_join_message',
                'user': self.user  # Include the joining user's name
            }
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group when the user disconnects
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive a message from WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')

        # Send the received message to all users in the room
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
        # Compare event['user'] with self.user to check if the current user is the one joining
        if event["user"] == self.user:
            # The user is the one who just joined, show them a personal message
            await self.send(text_data=json.dumps({
                'message': f'You have joined the chat',
                'user': 'Server',
                'message_type': 'join_message'
            }))
        else:
            # Send the join message to other users
            await self.send(text_data=json.dumps({
                'message': f'{event["user"]} has joined the chat',
                'user': 'Server',
                'message_type': 'join_message'
            }))

    async def chat_message(self, event):
        # Send a regular chat message to the WebSocket
        message = event['message']
        user = event['user']
        message_type = event['message_type']

        # Send the message to the WebSocket client
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'message_type': message_type
        }))
