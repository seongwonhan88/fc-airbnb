from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class NormalUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_host=False)


class HostUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_host=True)


class User(AbstractUser):
    #매니저 설정
    objects = models.Manager()
    user_objects = NormalUserManager()
    host_objects = HostUserManager()

    #공통 필드
    img_profile = models.ImageField(upload_to='user', blank=True)

    # USER 필드
    user_introduction = models.TextField(blank=True)
    saved_room = models.ManyToManyField('home.Room', related_name='saved_user')

    # HOST 관련 필드
    is_host = models.BooleanField(default=False)
    listings = models.ManyToManyField('home.Room', related_name='hosting')
    host_introduction = models.TextField(blank=True, null=True)


class NormalUser(User):
    class Meta:
        proxy = True


class HostUser(User):
    class Meta:
        proxy = True


