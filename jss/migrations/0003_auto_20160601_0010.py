# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 00:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jss', '0002_computer_operating_system'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer',
            old_name='operating_system',
            new_name='operating_systems',
        ),
    ]
