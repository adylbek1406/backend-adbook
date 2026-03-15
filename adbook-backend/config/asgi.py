import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import apps.chat.routing  # Will be created later

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/chat/<int:room_id>/", apps.chat.consumers.ChatConsumer.as_asgi()),
            # Notifications consumer later
        ])
    ),
})

