from django.urls import re_path
from .consumers import DraftConsumer  # Ensure the consumer is correctly imported

websocket_urlpatterns = [
    re_path(r'ws/draft/(?P<room_name>\w+)/$', DraftConsumer.as_asgi()),
]
