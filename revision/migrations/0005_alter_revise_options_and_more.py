# Generated by Django 4.0.4 on 2023-03-02 17:59

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_posts_created_by_alter_posts_modified_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('revision', '0004_revise_user_alter_revise_fifteenth_revision_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='revise',
            options={'get_latest_by': 'modified', 'ordering': ['-modified'], 'verbose_name': 'Revision', 'verbose_name_plural': 'Revisions'},
        ),
        migrations.AlterField(
            model_name='revise',
            name='fifteenth_revision_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 16, 17, 59, 5, 806907)),
        ),
        migrations.AlterField(
            model_name='revise',
            name='first_revision_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 3, 17, 59, 5, 806827)),
        ),
        migrations.AlterField(
            model_name='revise',
            name='last_revision_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 1, 17, 59, 5, 806919)),
        ),
        migrations.AlterField(
            model_name='revise',
            name='second_revision_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 17, 59, 5, 806858)),
        ),
        migrations.AlterField(
            model_name='revise',
            name='seventh_revision_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 9, 17, 59, 5, 806893)),
        ),
        migrations.AlterField(
            model_name='revise',
            name='third_revision_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 5, 17, 59, 5, 806879)),
        ),
        migrations.AlterIndexTogether(
            name='revise',
            index_together={('post', 'user')},
        ),
    ]
