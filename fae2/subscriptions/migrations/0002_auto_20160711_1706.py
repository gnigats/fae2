# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-11 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='token',
            field=models.CharField(default='', max_length=48),
        ),
        migrations.AlterField(
            model_name='payment',
            name='transaction_id',
            field=models.CharField(default='', max_length=13),
        ),
    ]