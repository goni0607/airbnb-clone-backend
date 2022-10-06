from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    email = models.EmailField(
        verbose_name="email address", unique=True, blank=True)
    name = models.CharField(max_length=150)
    is_host = models.BooleanField()
