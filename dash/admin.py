from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserPreferences
from .signals import *

# Register your models here.
class PreferencesInline(admin.StackedInline):
    model = UserPreferences
    can_delete = False
    verbose_name_plural = 'preferences'


# Register your models here.
class CustomUserAdmin(UserAdmin):
    inlines = (PreferencesInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserPreferences, admin.ModelAdmin)
