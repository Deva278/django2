import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp2.models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")
