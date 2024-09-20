from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.PROTECT)
    balance = models.FloatField(default = 0.0)
    requirements = models.TextField(null = True, blank = True)
    about = models.TextField(null = True, blank = True)
    speciality = models.CharField(max_length = 255, null = True, blank = True)
    role = models.CharField(max_length = 255)
    slug = models.SlugField(blank=True, null = True)
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('profile', kwargs = {'profile_slug': self.slug})
    def __str__(self):
        return self.user.username

