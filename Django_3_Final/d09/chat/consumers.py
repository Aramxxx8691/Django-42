import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.user = self.scope["user"].username

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Notify everyone except the joining user
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_join_message',
                'user': self.user
            }
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')

        # Send message to room group
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
        # Send a join notification to the WebSocket but with a message_type to indicate it’s a system message.
        await self.send(text_data=json.dumps({
            'message': f'{event["user"]} has joined the chat',
            'user': event["user"],
            'message_type': 'join_message'
        }))

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        message_type = event['message_type']

        # Send user message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'message_type': message_type
        }))
