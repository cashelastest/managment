from django import forms
from .models import *


class TaskForm(forms.ModelForm):
	title = forms.CharField(label = "Задача", widget = forms.TextInput(attrs = {"placeholder": "Назва задачи"}))
	class Meta:
		model = Task
		fields = ["title", "description", "important", "isDone", "layout", "connections"]
