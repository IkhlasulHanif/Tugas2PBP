from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.TextField()
    description = models.TextField(null = True)
    is_finished = models.BooleanField(default = False)
