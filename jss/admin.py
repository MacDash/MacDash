from django.contrib import admin
from .models import Computer, Site


class ComputerAdmin(admin.ModelAdmin):
    search_fields = ('name', 'serial_number')
    list_display = ('name', 'serial_number', 'mac_address')

    class Media:
        js = ('/static/js/admin.js',)

    def has_add_permission(self, request, obj=None):
        return False

class ComputersInline(admin.StackedInline):
    model = Computer
    can_delete = False
    verbose_name_plural = 'profile'
    show_change_link = True
    fields = ('computer_id', )
    read_only_fields = ('computer_id', )

class SiteAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    inlines = (ComputersInline, )

    class Media:
        js = ('/static/js/admin.js',)

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Computer, ComputerAdmin)
admin.site.register(Site, SiteAdmin)
