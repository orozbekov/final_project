from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField("Электронный адрес", unique=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['email']

    def __str__(self):
        return self.username

    objects = CustomUserManager()
