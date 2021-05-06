from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='media/avatars/')

class UserFiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    audios = models.FileField(upload_to='media/audios/')

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/images/', blank=True)



