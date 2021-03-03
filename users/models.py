from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class ExtendUser(AbstractUser):

    email = models.EmailField(blank=False, max_length=255, verbose_name="email")
    is_activated = models.BooleanField(default=True)
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    