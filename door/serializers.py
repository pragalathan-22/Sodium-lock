# from rest_framework import serializers

# class DoorSerializer(serializers.Serializer):
#     status = serializers.ChoiceField(choices=["open", "locked"])


from rest_framework import serializers

class DoorAccessSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    password = serializers.CharField(max_length=20)

class DoorAccessResponseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    password = serializers.CharField(max_length=20)
    status = serializers.CharField()
    open_time = serializers.DateTimeField()
    close_time = serializers.DateTimeField()
