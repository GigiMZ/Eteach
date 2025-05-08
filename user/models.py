from django.db import models
from django.contrib.auth.models import User as Usr


class User(Usr):
    age = models.PositiveIntegerField()
    profile_pic = models.ImageField(default="profile/default_S.jpg", blank=True, upload_to="profile/")
