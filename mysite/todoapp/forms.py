from wsgiref.headers import tspecials
from django import forms
from .models import Task, ToDoList

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'completed', 'notes']

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['todolist']