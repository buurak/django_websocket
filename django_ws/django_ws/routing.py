import os

from websocket.middlewares import WebSocketJWTAuthMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from websocket import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_ws.settings")


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": WebSocketJWTAuthMiddleware(URLRouter(routing.websocket_urlpatterns)),
    }
)
