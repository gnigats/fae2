# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-21 00:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0018_auto_20161020_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institutionalsubscription',
            name='account_type',
        ),
        migrations.RemoveField(
            model_name='institutionalsubscription',
            name='users',
        ),
        migrations.DeleteModel(
            name='InstitutionalSubscription',
        ),
    ]
