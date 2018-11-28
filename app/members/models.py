from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    img_profile = models.ImageField(upload_to='user', blank=True)
    user_introduction = models.TextField(blank=True, null=True)
    saved_room = models.ManyToManyField('home.Room', related_name='saved_user')
