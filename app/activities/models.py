from django.db import models
from user_manager.models import User


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_activity", default=None)
    message = models.CharField(default=None, max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activity'