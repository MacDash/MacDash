# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jss', '0004_auto_20160529_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='applications',
            field=models.ManyToManyField(max_length=200, to='jss.ComputerApplication'),
        ),
    ]