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
    archived = models.BooleanField(default=False, blank=True)

    def __str__(self): return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, validators=[validators.tag_validator])
    posts = models.ManyToManyField(Post, blank=True, related_name='tags')

    def __str__(self): return self.name


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    vote_up = models.PositiveIntegerField(default=0)
    vote_down = models.PositiveIntegerField(default=0)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    comment = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    def __str__(self):
        if len(str(self.content)) > 20: return f'{self.content[:20]}...'
        return self.content



class Category(models.Model):
    name = models.CharField(max_length=70, unique=True)
    posts = models.ManyToManyField(Post, related_name='categories', null=True, blank=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategories',
                                       null=True, blank=True)

    def __str__(self): return self.name

    class Meta:
        verbose_name_plural = 'categories'
