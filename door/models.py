# from django.db import models

# class DoorAccess(models.Model):
#     password = models.CharField(max_length=20)
#     status = models.CharField(max_length=10, choices=[('open', 'Open'), ('locked', 'Locked')])
#     open_time = models.DateTimeField()
#     close_time = models.DateTimeField()

#     def __str__(self):
#         return f"User {self.user_id} - {self.status} at {self.open_time}"

# # models.py
# from django.db import models

# class DoorAccess(models.Model):
#     user_id = models.IntegerField(default=0)  # ✅ Set a default value
#     password = models.CharField(max_length=20)
#     status = models.CharField(max_length=10, choices=[('open', 'Open'), ('locked', 'Locked')])
#     open_time = models.DateTimeField()
#     close_time = models.DateTimeField()

from django.db import models

class DoorAccess(models.Model):
    user_id = models.IntegerField(default=0)  # Optional, useful if needed later
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=[('open', 'Open'), ('locked', 'Locked')])
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()

    def __str__(self):
        return f"Access #{self.id} - {self.status}"

