from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserPreferences

@receiver(post_save, sender=User)
def create_userpreferences(sender, created, instance, **kwargs):
    if created:
        userpreferences = UserPreferences.objects.create(user=instance)
        instance.userpreferences = userpreferences
        instance.save()