from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    phone = models.CharField(max_length=15, blank=False, null=False, unique=True)

    def __str__(self):
        return f'{self.phone} {self.username} {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

