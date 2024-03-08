"""
ASGI config for django_assignment project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_assignment.settings')

# application = get_asgi_application()
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from feeds.consumers import LiveFeedConsumer

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    "websocket": URLRouter([
        path("ws/live-feed/", LiveFeedConsumer.as_asgi()),
    ]),
})