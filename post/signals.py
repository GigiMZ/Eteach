from .models import Post
from django.db.models.signals import post_delete
from django.dispatch import receiver

import os
from dotenv import load_dotenv


@receiver(post_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    load_dotenv()
    image = instance.image
    if not image:
        print("No picture to Delete.")
        return
    dir = os.getenv("DIR")
    os.remove(f'{dir}\\media\\{image}')
    if not os.path.exists(f'{dir}\\media\\{image}'):
        print("Deleted successfully!")
        return
    print("Couldn't Delete.")
