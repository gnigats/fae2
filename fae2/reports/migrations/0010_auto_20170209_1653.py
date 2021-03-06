# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-09 22:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_auto_20170109_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcludedURL',
            fields=[
                ('filtered_url_id', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.CharField(default=b'', max_length=256, verbose_name=b'File Type')),
                ('url', models.URLField(max_length=4096, verbose_name=b'Other URL')),
                ('url_referenced', models.URLField(max_length=4096, verbose_name=b'Referenced URL')),
                ('file_type', models.CharField(default=b'', max_length=16, verbose_name=b'File Type')),
            ],
            options={
                'ordering': ['url_referenced', 'url'],
                'verbose_name': 'URL: Excluded',
                'verbose_name_plural': 'URL: Excluded',
            },
        ),
        migrations.AlterField(
            model_name='websitereport',
            name='max_pages',
            field=models.IntegerField(choices=[(5, b'   5 pages'), (10, b'  10 pages'), (25, b'  25 pages'), (50, b'  50 pages'), (100, b' 100 pages'), (200, b' 200 pages'), (400, b' 400 pages'), (800, b' 800 pages')], default=0, verbose_name=b'Evaluation Limited To'),
        ),
        migrations.AddField(
            model_name='excludedurl',
            name='ws_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='excluded_urls', to='reports.WebsiteReport'),
        ),
    ]
