from django.contrib.auth.models import AbstractUser
from django.db import models

from home.models import Room


class User(AbstractUser):
    img_profile = models.ImageField(upload_to='user', blank=True)
    user_introduction = models.TextField()


class HostThumbnailImg(models.Model):
    # One To One 모델로 바꾸기
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name='host_thumbnails', )
    host_thumbnail_url = models.ImageField(upload_to='pictures/host/', blank=True, null=True)
    host_thumbnail_url_small = models.ImageField(upload_to='pictures/host/', blank=True, null=True)
