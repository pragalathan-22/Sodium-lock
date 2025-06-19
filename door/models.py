from django.db import models

class DoorAccess(models.Model):
    user_id = models.IntegerField()
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=[('open', 'Open'), ('locked', 'Locked')])
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()

    def __str__(self):
        return f"User {self.user_id} - {self.status} at {self.open_time}"
