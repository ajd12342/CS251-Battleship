from django.urls import path,include

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from . import consumers

# application = ProtocolTypeRouter({
#
#     "websocket": AuthMiddlewareStack(
#         path('/ws/users/',consumers.ChatConsumer)
#     ),
#
# })
websocket_urlpatterns = [
    path('users/',consumers.ChatConsumer),
]