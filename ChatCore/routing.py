from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from chat import consumer

# urls that handles the websocket connection is put here
websocket_urlpatterns=[
    re_path(
        r"ws/chat/(?P<chat_box_name>\w+)/$", consumer.ChatRoomConsumer.as_asgi()
    ),
]

application = ProtocolTypeRouter( 
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)
