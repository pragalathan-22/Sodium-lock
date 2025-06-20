# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .serializers import DoorSerializer

# # Global door command state
# door_command = {"status": "locked"}

# def index(request):
#     return render(request, "index.html")  # Load the web page

# @api_view(['GET', 'POST'])
# def door_api(request):
#     global door_command

#     if request.method == 'POST':
#         serializer = DoorSerializer(data=request.data)
#         if serializer.is_valid():
#             # Update door status
#             door_command['status'] = serializer.validated_data['status']
#             return Response({'message': 'Command received', 'status': door_command['status']})
#         return Response(serializer.errors, status=400)

#     elif request.method == 'GET':
#         # Auto-lock after returning 'open' once
#         current_status = door_command['status']
#         if current_status == 'open':
#             door_command['status'] = 'locked'
#         return Response({'status': current_status})

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DoorAccessSerializer, DoorAccessResponseSerializer
from .models import DoorAccess
from django.utils import timezone
from datetime import timedelta


# Door lock state
door_command = {"status": "locked"}

def index(request):
    return render(request, "index.html")

@api_view(['POST', 'GET'])
def door_api(request):
    global door_command

    if request.method == 'POST':
        serializer = DoorAccessSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            password = serializer.validated_data['password']

            # ✅ Check if user+password exists in database
            existing_user = DoorAccess.objects.filter(user_id=user_id, password=password).exists()

            if existing_user or DoorAccess.objects.filter(user_id=user_id).count() == 0:
                # Allow access if user already exists with correct password
                # OR this is a new user (first-time setup)

                open_time = timezone.now()
                close_time = open_time + timedelta(seconds=10)

                # Change door status to open
                door_command['status'] = 'open'

                # Save access log
                DoorAccess.objects.create(
                    user_id=user_id,
                    password=password,
                    status='open',
                    open_time=open_time,
                    close_time=close_time
                )

                return Response({
                    "user_id": user_id,
                    "password": password,
                    "status": "open",
                    "open_time": open_time,
                    "close_time": close_time
                })

            return Response({"error": "Invalid password for this user ID"}, status=400)

        return Response(serializer.errors, status=400)

    elif request.method == 'GET':
        # ESP32 or frontend fetches door status
        current_status = door_command['status']
        if current_status == 'open':
            door_command['status'] = 'locked'
        return Response({'status': current_status})
