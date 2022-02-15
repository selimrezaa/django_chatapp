from django.urls import path 
from app import consumers

websocket_urlpatterns = [
    path('ws/sc/<str:groupkanam>/', consumers.MySyncConsumer.as_asgi()),
]