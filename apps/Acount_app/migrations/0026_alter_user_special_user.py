# Generated by Django 4.1 on 2022-08-28 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0025_user_special_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 13, 21, 23, 444613, tzinfo=datetime.timezone.utc)),
        ),
    ]
