from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from   
 .models import MyModel

def my_caller():
    with transaction.atomic():
        model_instance = MyModel.objects.create(field1="value1", field2="value2")

        # Do something that might cause a rollback
        raise Exception("Intentional error to trigger rollback")

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    # Try to create another model object
    try:
        OtherModel.objects.create(related_model=instance)
    except Exception as e:
        print("Error in signal handler:", e)