from django import forms
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class RegisterForm(UserCreationForm):
	username = forms.CharField(label = "Юзер")
	password1 = forms.CharField(label = 'pass', widget = forms.PasswordInput(attrs = {"class":"char", "placeholder":"pass1"}))
	password2 = forms.CharField(label = 'pass', widget = forms.PasswordInput(attrs = {"class":"char", "placeholder":"pass2"}))

	class Meta:
		model = get_user_model()
		fields = ("username", "password1","password2")	