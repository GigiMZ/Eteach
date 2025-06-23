from django.db import models
from django.contrib.auth.models import AbstractUser

from post.models import Post, Comment


class User(AbstractUser):
    private = models.BooleanField(default=False)
    age = models.PositiveIntegerField(default=0)
    profile_pic = models.ImageField(default="profile/default_S.jpg", blank=True, upload_to="profile/")
    up_voted_posts = models.ManyToManyField(Post, related_name="users_up_voted", blank=True)
    down_voted_posts = models.ManyToManyField(Post, related_name="users_down_voted", blank=True)
    up_voted_comments = models.ManyToManyField(Comment, related_name="users_up_voted", blank=True)
    down_voted_comments = models.ManyToManyField(Comment, related_name="users_down_voted", blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
