from .models import User
from post.models import Post, Comment
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db.models import F

import os
from dotenv import load_dotenv


@receiver(post_delete, sender=User)
def delete_prof_pic(sender, instance, **kwargs):
    load_dotenv()
    pic = instance.profile_pic
    dir = os.getenv("DIR")
    if pic != 'profile/default_S.jpg': os.remove(f'{dir}\\media\\{pic}')
    if not os.path.exists(f'{dir}\\media\\{pic}'):
        print("Deleted successfully!")
        return
    print("Not Deleted or default.")

@receiver(post_delete, sender=User)
def post_archive_comments_delete(sender, instance, **kwargs):
    # archiving posts
    for post in Post.objects.filter(author=instance):
        post.archived = True
        post.save()
    # deleting comments
    for comment in Comment.objects.filter(author=instance):
        comment.delete()
    print('yez')

@receiver(post_delete, sender=User)
def vote_remove(sender, instance, **kwargs):
    instance.up_voted_posts.all().vote_up = F('vote_up') - 1
    instance.down_voted_posts.all().vote_down = F('vote_down') - 1
    instance.up_voted_comments.all().vote_up = F('vote_up') - 1
    instance.down_voted_comments.all().vote_down = F('vote_down') - 1
    print('hello')
