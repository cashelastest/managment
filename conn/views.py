from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
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

	success_url = reverse_lazy("home")
class Show(ListView):
	model = Task

	template_name = "conn/show.html"


	def get_context_data(self, object_list=None, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		tasks = Task.objects.all()
		all_finishes = tasks.filter(isFinish=True).count()
		def count_final_tasks_iteratively(task):
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
			task.toGoal = total_finals

			# if all_finishes/3<=task.toGoal<=(all_finishes*2)/3:
			# 	task.color = "yellow"
			# elif task.toGoal<all_finishes/3:
			# 	task.color = "red"
			# 	print("red")
			# else:
			# 	task.color = "green"

			task.save()
			return total_finals
		
		# Для каждого таска вызываем функцию
		for task in tasks:
			count_final_tasks_iteratively(task)

		# Добавляем выбранные значения в контекст
		context['layouts'] = Layout.objects.all()
		selected_layouts = self.request.GET.getlist('layout')
		print(selected_layouts)
		if selected_layouts:
			context['tasks'] = tasks.filter(layout__id__in = selected_layouts)

		else:
			context['tasks'] = tasks
		print(tasks)
		return context

	def post(self, request, *args, **kwargs):
		node_id = request.POST.get('node_id')
		new_color = request.POST.get('new_color')
		text_color = request.POST.get("text_color")
		border_color = request.POST.get("border_color")
		
		try:
			task = Task.objects.get(id=node_id)
			task.color = new_color
			task.textColor = text_color
			task.borderColor  = border_color 
			print(f"{task.color}" + f"{task.title}")
			task.save()
			return JsonResponse({'status': 'success'})
		except Task.DoesNotExist:
			return JsonResponse({'status': 'error', 'message': 'Node not found'})