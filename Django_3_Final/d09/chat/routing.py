from django.urls import re_path
from . import consumers  # Adjust the import based on your project structure

websocket_urlpatterns = [
    re_path(r'ws/chat/global/$', consumers.GlobalChatConsumer.as_asgi(), name='global_chat'),
    re_path(r'ws/chat/(?P<room_name>[^/]+)/$', consumers.PrivateChatConsumer.as_asgi(), name='private_chat'),
]
