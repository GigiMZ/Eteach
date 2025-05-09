from .models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

import os
from dotenv import load_dotenv


@receiver(post_delete, sender=User)
def delete_prof_pic(sender, instance, **kwargs):
    load_dotenv()
    pic = instance.profile_pic
    print(pic)
    dir = os.getenv("DIR")
    if pic != 'profile/default_S.jpg': os.remove(f'{dir}\\media\\{pic}')
    if not os.path.exists(f'{dir}\\media\\{pic}'):
        print("Deleted successfully!")
        return
    print("Not Deleted or default.")
