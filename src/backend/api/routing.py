from django.urls import re_path

from backend.api.consumers import TimeConsumer

websocket_urlpatterns = [
    re_path(r"ws/time/$", TimeConsumer.as_asgi()),
]
