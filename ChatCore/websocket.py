from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
# import app.routing
from django.urls import path, re_path

from chat.consumer import ChatConsumer

# websocket_urlpatterns = [
#     path('ws/<room_name>/$', cha.as_asgi()),
# ]

application = ProtocolTypeRouter({
    'websocket':AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                re_path(r'chat/', ChatConsumer.as_asgi()),
            ])
        )
    ),
})