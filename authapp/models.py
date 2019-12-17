from django.db import models
from django.contrib.auth.models import AbstractUser


class BorshchUser(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    avatar = models.ImageField(upload_to='users_avatars', blank=True)

    def __str__(self):
        return self.username