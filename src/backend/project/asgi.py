"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from contextlib import asynccontextmanager

from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from django.core.asgi import get_asgi_application

from backend.api.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.project.settings")


@asynccontextmanager
async def lifespan(app):
    """ASGI lifespan protocol support."""
    # Perform one-time startup operations here (e.g., connecting to a database, caches)
    yield
    # Perform one-time shutdown operations here (e.g., closing a database connection)


# Wrap Django's ASGI application
class LifespanMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "lifespan":
            async with lifespan(self.app):
                while True:
                    message = await receive()
                    if message["type"] == "lifespan.startup":
                        await send({"type": "lifespan.startup.complete"})
                    elif message["type"] == "lifespan.shutdown":
                        break
            await send({"type": "lifespan.shutdown.complete"})
        else:
            await self.app(scope, receive, send)


django_asgi_app = get_asgi_application()
application = LifespanMiddleware(
    ProtocolTypeRouter(
        {
            "http": django_asgi_app,
            "websocket": URLRouter(websocket_urlpatterns),
        },
    ),
)
