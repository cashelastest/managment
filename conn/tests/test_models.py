from django.test import TestCase
from conn.models import *


class TestModels(TestCase):
	def setUp(self):
		self.Task1 = Task.objects.create(
			title = "TestTask",
			description = "Some description test",
			important = 0.3,
			)
		self.Task2 = Task.objects.create(
			title = "TestTask2",
			description = "Some another description test",
			important = 0.4,
			)
		self.Task3 = Task.objects.create(
			title = "TestTask3",
			description = "Some another description test",
			important = 0.4,
			)
		self.Task4 = Task.objects.create(
			title = "TestTask4",
			description = "Some another description test",
			important = 0.4,
			)
		self.Task5 = Task.objects.create(
			title = "TestTask5",
			description = "Some another description test",
			important = 0.4,
			)
		self.connector13 = Connector.objects.create(

			startTask = self.Task1,
			finishTask = self.Task3,
			isFinish = False,
			isStart = True
			)
		self.connector35 = Connector.objects.create(

			startTask = self.Task3,
			finishTask = self.Task5,
			isFinish = True
			)
		self.connector34 = Connector.objects.create(

			startTask = self.Task4,
			finishTask = self.Task5,
			isStart = True,
			isFinish = True
			)
		self.connector4 = Connector.objects.create(

			startTask = self.Task2,
			finishTask = self.Task3,
			isStart = True,
			isFinish = True
			)

	def test_creating_connector(self):
		connector = Connector.objects.create(
			startTask = self.Task1,
			finishTask = self.Task2
			)
		connector1= Connector.objects.create(
			startTask = self.Task2,
			finishTask = self.Task3,
			isFinish = True
			)
		connector2= Connector.objects.create(
			startTask = self.Task1,
			finishTask = self.Task2,
			isFinish = False
			)

		print(f"\n\x1b[30;42m COMPLETE \x1b[0m")


	def test_counting(self):
		connectors = Connector.objects.filter(startTask=self.Task2)
		
		def find_paths(current, path, all_paths, finishes):
			path.append(current)  # Добавляем текущее соединение в путь
			if current.isFinish:
				all_paths.append(list(path))
				if current.finishTask not in finishes:
					finishes.append(current.finishTask)  # Копируем путь и добавляем в список всех путей
			else:
				next_connectors = Connector.objects.filter(startTask=current.finishTask)
				for next_connector in next_connectors:
					if next_connector not in path:  # Проверка на зацикливание
						find_paths(next_connector, path, all_paths,finishes)
			path.pop()  # Удаляем текущее соединение из пути для других путей

		all_paths = []
		finishes = []
		for start in connectors:
			find_paths(start, [], all_paths, finishes)
		
		for path in all_paths:
			print(f"Start: {path[0].startTask.title}--->")
			print([f"{connector.finishTask}  =>" for connector in path])
			print(len(path))

		print(f"FINISHES: {finishes}")
		print(sum([task.important for task in finishes]))