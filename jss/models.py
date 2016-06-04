from django.db import models

# Create your models here.
class Site(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class ComputerApplication(models.Model):
    name = models.CharField(max_length=300)
    path = models.CharField(max_length=800)
    version = models.CharField(max_length=400, null=True)

    def __str__(self):
        return '{name}_{version}'.format(name=self.name, version=self.version)


class Computer(models.Model):
    computer_id = models.CharField(max_length=100000, null=True)
    alt_mac_address = models.CharField(max_length=20, null=True)
    asset_tag = models.CharField(max_length=200, null=True)
    barcode_1 = models.CharField(max_length=200, null=True)
    barcode_2 = models.CharField(max_length=200, null=True)
    distribution_point = models.CharField(max_length=400, null=True)
    initial_entry_date_utc = models.DateField(null=True)
    ip_address = models.CharField(max_length=15, null=True)
    itunes_store_account_is_active = models.NullBooleanField()
    jamf_version = models.CharField(max_length=200, null=True)
    last_contact_time_utc = models.DateTimeField(null=True)
    mac_address = models.CharField(max_length=200, null=True)
    mdm_capable = models.NullBooleanField()
    mdm_capable_users = models.TextField(null=True)
    name = models.CharField(max_length=200)
    netboot_server = models.CharField(max_length=200, null=True)
    platform = models.CharField(max_length=200, null=True)
    remote_management = models.TextField(null=True)
    report_date_utc = models.DateField(null=True)
    serial_number = models.CharField(max_length=200, null=True)
    warranty_expires_utc = models.DateField(null=True)
    os_version = models.CharField(max_length=200, null=True)
    model = models.CharField(max_length=200, null=True)
    total_ram_mb = models.CharField(max_length=200, null=True)
    real_name = models.CharField(max_length=200, null=True)
    building = models.CharField(max_length=200, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, related_name='computers')
    applications = models.ManyToManyField(ComputerApplication, max_length=200, related_name='computers')

    def __str__(self):
        return self.name
