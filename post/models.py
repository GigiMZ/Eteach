from django.db import models
from django.conf import settings
from . import validators


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, validators=[validators.title_validator])
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="post/")
    date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    vote_up = models.PositiveIntegerField(default=0)
    vote_down = models.PositiveIntegerField(default=0)

    def __str__(self): return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, validators=[validators.tag_validator])
    posts = models.ManyToManyField(Post, blank=True)

    def __str__(self): return self.name


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    vote_up = models.PositiveIntegerField(default=0)
    vote_down = models.PositiveIntegerField(default=0)
    post = models.ForeignKey(Post, null=True, blank=True, related_name="comments", on_delete=models.CASCADE) # TODO null/blank
    comment = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    def __str__(self): return self.content[:20]
