# Generated by Django 4.1 on 2022-09-04 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0029_techer_is_active_alter_user_special_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='techer',
            old_name='is_active',
            new_name='is_activee',
        ),
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 4, 15, 35, 14, 997179, tzinfo=datetime.timezone.utc)),
        ),
    ]
