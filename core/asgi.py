import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.layers import get_channel_layer
import ride.routing 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings") 

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            ride.routing.websocket_urlpatterns 
        )
    ),
})
