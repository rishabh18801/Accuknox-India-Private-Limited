from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender,   
 instance, **kwargs):
    # Do something synchronous here
    print("Signal handler executed synchronously")
