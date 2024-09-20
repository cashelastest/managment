from django.shortcuts import render
from users.models import *
from django.views.generic import ListView, CreateView, DetailView
from .forms import  *
from django.urls import reverse_lazy
class Home(DetailView):
	model = Profile
	slug_url_kwarg = 'profile_slug'
	context_object_name = "profile"
	template_name = "users/profile.html"

class Registration(CreateView):
    form_class = UserCreationForm  # Форма для регистрации
    template_name = 'users/sign_up.html'  # Шаблон
    success_url = reverse_lazy('users:login')  # URL для перенаправления после успешной регистрации

    def form_valid(self, form):
        # Сохраняем пользователя
        user = form.save()
        
        # Создаем профиль, если его не существует
        if not Profile.objects.filter(user=user).exists():
            Profile.objects.create(user=user)

        return super().form_valid(form)
# Create your views here.
