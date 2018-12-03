from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    img_profile = models.ImageField(upload_to='user', blank=True)
    user_introduction = models.TextField(blank=True)
    saved_room = models.ManyToManyField('home.Room', related_name='saved_user')
    is_host = models.BooleanField(default=False)


class Host(User):
    rating = models.PositiveIntegerField(default=4)
    listings = models.ManyToManyField('home.Room', related_name='hosting')
