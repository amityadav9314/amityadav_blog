# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
