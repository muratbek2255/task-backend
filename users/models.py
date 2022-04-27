from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """Кастомная модель для пользователя"""
    username = None
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    age = models.PositiveSmallIntegerField(null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
