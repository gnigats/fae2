# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-05 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0008_auto_20160804_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='redirect_url',
            field=models.URLField(blank=True, max_length=256),
        ),
    ]
