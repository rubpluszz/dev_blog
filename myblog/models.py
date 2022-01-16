from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.SlugField()
    descripyion = models.TextField()
    image = models.ImageField()
    created_at = models.DateField(default=timezone.now)
    tag = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
