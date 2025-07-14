from .models import User


# getting list of users followers ids
def get_followers_id(user: User) -> list[int]:
    following_qs = User.following.through.objects.all().filter(to_user_id=user.id)
    return following_qs.values_list('from_user_id', flat=True)
