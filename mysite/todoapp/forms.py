from wsgiref.headers import tspecials
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'completed', 'notes']