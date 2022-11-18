from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=15, unique=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')