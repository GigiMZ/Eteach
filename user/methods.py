from .models import User
from django.db.models import QuerySet


def get_followers(user: User) -> QuerySet:
    following_qs = User.following.through.objects.all().filter(to_user_id=user.id)
    followers_list = following_qs.values_list('from_user_id', flat=True)
    return User.objects.filter(id__in=followers_list)