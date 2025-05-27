from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    profile_pic = models.ImageField(default="profile/default_S.jpg", blank=True, upload_to="profile/")
