# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-17 21:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0014_auto_20161017_1548'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InstitionalSubscription',
            new_name='InstitutionalSubscription',
        ),
    ]