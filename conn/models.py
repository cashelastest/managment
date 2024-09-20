from django.db import models
from django.utils.text import slugify
from users.models import *
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
	requirement_skills = models.TextField(default = "No special skills")
	weight = models.FloatField()
	isDone = models.BooleanField(default = False)
	previous_connections = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='related_tasks')
	workers = models.ManyToManyField(Profile, null =True)
	deadline = models.DateTimeField(null = True, blank = True)
	started = models.DateTimeField(null = True, blank = True)
	price = models.FloatField(null = True)
	isStart = models.BooleanField(default = False)
	isFinish = models.BooleanField(default = False)


	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		return super(Task, self).save(*args,**kwargs)
	def __str__(self):
		return self.title

