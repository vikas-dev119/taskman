from django.db import models
from datetime import datetime
from django.utils import timezone 
from user_manager.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_task", default=None)
    name = models.CharField(max_length=50, default=None, blank=False, null=False)
    deadline = models.DateTimeField(default=datetime.now())
    status = models.IntegerField(default=0, blank=True, null=True, help_text='1->Active, 0->Inactive' )
    created_on = models.DateTimeField(default=datetime.now(), blank=True)

    class Meta:
        db_table = 'task'