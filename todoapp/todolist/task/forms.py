from django import forms
from django.forms import ModelForm
from .models import *

# Create the form class.
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'completed']
