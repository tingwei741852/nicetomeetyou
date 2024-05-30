from django.urls import path
from .views import NewsConsumer

websocket_urlpatterns = [
    path('ws/news/', NewsConsumer.as_asgi()),
]