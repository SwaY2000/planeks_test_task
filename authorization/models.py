from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username
