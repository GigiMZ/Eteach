from user.models import User
from user.methods import get_followers
from .models import Post

from django.db.models import QuerySet


def get_posts(user: User) -> QuerySet:
    allowed_users_id: set[int] = set()
    allowed_users_id.update(list(User.objects.filter(private=False).values_list('id', flat=True)))
    allowed_users_id.update(list(get_followers(user).values_list('id', flat=True)))
    return Post.objects.filter(author_id__in=allowed_users_id)
