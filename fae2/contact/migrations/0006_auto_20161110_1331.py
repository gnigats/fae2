# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-10 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20161007_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='message_text',
            field=models.TextField(blank=True, default=b''),
        ),
    ]