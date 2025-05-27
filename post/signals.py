from .models import Post
from django.db.models.signals import post_delete
from django.dispatch import receiver

import os
from dotenv import load_dotenv


@receiver(post_delete, sender=Post)
def delete_prof_pic(sender, instance, **kwargs):
    load_dotenv()
    pic = instance.image
    if not pic:
        print("No picture to Delete.")
        return
    dir = os.getenv("DIR")
    os.remove(f'{dir}\\media\\{pic}')
    if not os.path.exists(f'{dir}\\media\\{pic}'):
        print("Deleted successfully!")
        return
    print("Couldn't Delete.")
