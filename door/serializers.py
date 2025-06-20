# from rest_framework import serializers

# class DoorSerializer(serializers.Serializer):
#     status = serializers.ChoiceField(choices=["open", "locked"])


# serializers.py
from rest_framework import serializers
from .models import DoorAccess

class DoorAccessSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    password = serializers.CharField(max_length=20)

class DoorAccessResponseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    password = serializers.CharField(max_length=20)
    status = serializers.CharField()
    open_time = serializers.DateTimeField()
    close_time = serializers.DateTimeField()

# ✅ New simplified list serializer
class DoorAccessListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorAccess
        fields = ['id', 'password', 'open_time', 'close_time']

