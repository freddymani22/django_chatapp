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
django.setup()
from django.urls import path
django_asgi_app=get_asgi_application()

from chatapp import consumers

application = ProtocolTypeRouter({
    'http':django_asgi_app ,
    'websocket': AuthMiddlewareStack(
        URLRouter(
           [
                path('ws/<str:room_name>/',consumers.ChatConsumer.as_asgi()),
                path('ws/private-message/<int:id>/<int:other_id>/',consumers.PrivateMessageConsumer.as_asgi())
]
        )


    )
})
