from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    notes = models.TextField(default=None, null=True, blank=True)
