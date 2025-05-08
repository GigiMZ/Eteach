from django.db import models
from user.models import User


class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="post/")
    date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    vote_up = models.PositiveIntegerField(default=0)
    vote_down = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)
    comment = models.ForeignKey('Comment', null=True, blank=True, related_name="posts", on_delete=models.CASCADE)

    def __str__(self): return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self): return self.name


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    vote_up = models.PositiveIntegerField(default=0)
    vote_down = models.PositiveIntegerField(default=0)
    comment = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    def __str__(self): return self.content
