# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170717_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='customer',
        ),
        migrations.AddField(
            model_name='blog',
            name='subscribe',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Subscribe',
        ),
    ]
