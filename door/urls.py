from django.urls import path
from .views import door_api, index,door_access_list ,admin_panel,door_access_detail

urlpatterns = [
    path('', index),  # ✅ Load HTML
    path('api/door/', door_api),  # API for ESP32 and frontend
    path('api/list/', door_access_list), 
    path('admin-panel/',admin_panel, name='admin_panel'),  # ✅ New admin page
    path('api/door/<int:id>/', door_access_detail),
]
