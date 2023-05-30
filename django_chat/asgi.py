"""
ASGI config for django_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_chat.settings')
import django
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chatapp.routing



django.setup()


application = ProtocolTypeRouter({
    'https': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chatapp.routing.websocket_urlpatterns
        )


    )
})
