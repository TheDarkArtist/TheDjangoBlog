from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile = models.ImageField(upload_to='static/uploads/', null=True, blank=True)

