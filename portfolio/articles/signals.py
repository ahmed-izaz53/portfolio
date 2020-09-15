from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete

from .models import Article

@receiver(post_delete, sender=Article)
def on_delete(sender, **kwargs):
    instance = kwargs["instance"]
    instance.picture.delete(save=False)