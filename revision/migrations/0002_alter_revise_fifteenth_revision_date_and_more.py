# Generated by Django 4.0.4 on 2022-08-13 23:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revision', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revise',
            name='fifteenth_revision_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 23, 21, 52, 769621)),
        ),
        migrations.AlterField(
            model_name='revise',
            name='first_revision_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 14, 23, 21, 52, 769483)),
        ),
        migrations.AlterField(
            model_name='revise',
            name='last_revision_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 12, 23, 21, 52, 769635)),
        ),
        migrations.AlterField(
            model_name='revise',
            name='second_revision_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 15, 23, 21, 52, 769573)),
        ),
        migrations.AlterField(
            model_name='revise',
            name='seventh_revision_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 20, 23, 21, 52, 769606)),
        ),
        migrations.AlterField(
            model_name='revise',
            name='third_revision_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 16, 23, 21, 52, 769591)),
        ),
    ]