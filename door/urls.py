from django.urls import path
from .views import door_api, index

urlpatterns = [
    path('', index),  # ✅ Load HTML
    path('api/door/', door_api),  # API for ESP32 and frontend
]
