from django.db import models
from django.utils.text import slugify
class Layout(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField()
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		return super(Layout, self).save(*args, **kwargs)
	def __str__(self):
		return self.name
class Task(models.Model):
	title = models.CharField(max_length = 255)
	slug = models.SlugField()
	description = models.TextField()
	important = models.FloatField()
	isDone = models.BooleanField(default = False)
	connections = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='related_tasks')
	isStart = models.BooleanField(default = False)
	isFinish = models.BooleanField(default = False)
	toGoal = models.PositiveIntegerField(default = 0)
	color = models.CharField(max_length= 255, default = "green")
	layout = models.ManyToManyField(Layout, null = True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		return super(Task, self).save(*args,**kwargs)
	def __str__(self):
		return self.title


class Connector(models.Model):
	startTask = models.ForeignKey(Task, on_delete = models.CASCADE, related_name = "start",verbose_name = "start")
	finishTask = models.ForeignKey(Task, related_name = "finish",on_delete =models.CASCADE)

	isFinish = models.BooleanField(default = False)
