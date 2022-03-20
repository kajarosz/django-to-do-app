from django.db import models

# Create your models here.

class ToDoList(models.Model):
    todolist = models.CharField(max_length=200)

class Task(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    notes = models.TextField(default=None, null=True, blank=True)
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE, default=1)
