# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelreg', '0009_auto_20171024_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='casemessage',
            name='sender',
            field=models.CharField(choices=[('admin', 'Administrator'), ('finder', 'Finder'), ('owner', 'Owner')], default='admin', max_length=10),
            preserve_default=False,
        ),
    ]
