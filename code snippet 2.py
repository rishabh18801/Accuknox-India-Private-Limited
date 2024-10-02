import threading
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MyModel

def my_caller():
    # Create and save a MyModel object
    model_instance = MyModel.objects.create(field1="value1", field2="value2")

    # Print the current thread ID
    print("Caller thread ID:", threading.get_ident())

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    # Print the current thread ID
    print("Signal handler thread ID:", threading.get_ident())