import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import video_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zoom_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            video_app.routing.websocket_urlpatterns
        )
    ),
})
