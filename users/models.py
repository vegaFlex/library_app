from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_reader = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

