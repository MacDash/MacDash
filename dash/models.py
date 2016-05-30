from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPreferences(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        unique=True,
        primary_key=True,
        related_name='userpreferences',
    )
    display_sidebar = models.BooleanField(default=True)

    def __str__(self):              # __unicode__ on Python 2
        return "%s user preferences" % self.user.username