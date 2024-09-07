from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import *
class addTask(CreateView):
	form_class = TaskForm
	template_name = "conn/add_task.html"
	success_url = reverse_lazy("home")
class addLayout(CreateView):
	model = Layout
	fields = ['name']
	template_name = 'conn/add_layout.html'
	success_url = reverse_lazy("home")
class addConnector(CreateView):
	model = Connector
	fields = ("__all__")
	template_name = "conn/add_connector.html"
	success_url = reverse_lazy("home")
class Show(ListView):
	model = Task

	template_name = "conn/show.html"


	def get_context_data(self, object_list=None, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		tasks = Task.objects.all()
		all_finishes = tasks.filter(isFinish=True).count()
		def count_final_tasks_iteratively(task):
			""" Итеративная версия для подсчета финальных тасков """

			stack = [task]
			visited = set()
			total_finals = 0
			
			while stack:
				current_task = stack.pop()
				
				if current_task in visited:
					continue
				visited.add(current_task)
				if task.isFinish:
					return 0

				if current_task.isFinish:
					total_finals += 1
				else:
					stack.extend(current_task.connections.all())
			
			# Сохраняем результат в поле toGoal
			task.toGoal = total_finals
			if all_finishes/3<=task.toGoal<=(all_finishes*2)/3:
				task.color = "yellow"
			elif task.toGoal<all_finishes/3:
				task.color = "red"
				print("red")
			else:
				task.color = "green"
			task.save()
			return total_finals
		
		# Для каждого таска вызываем функцию
		for task in tasks:
			count_final_tasks_iteratively(task)
		selected_layouts = self.request.GET.getlist('layout')
		print(selected_layouts)
		# Добавляем выбранные значения в контекст
		context['layouts'] = Layout.objects.all()
		
		# Логика фильтрации по выбранным значениям

		return context

