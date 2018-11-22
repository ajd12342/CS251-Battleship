from django.urls import path,include

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from pairing.consumers import ChatConsumer
from play.consumers import SubmitConsumer,GameConsumer,GameChatConsumer
websocket_urlpatterns = [
    path('users/',ChatConsumer),
    path('placing/',SubmitConsumer),
    path('game/',GameConsumer),
    path('chat/',GameChatConsumer),
]