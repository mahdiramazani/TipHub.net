# Generated by Django 4.1 on 2022-09-04 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0027_alter_user_special_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='techer',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='teacher/cv'),
        ),
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 4, 13, 10, 21, 155965, tzinfo=datetime.timezone.utc)),
        ),
    ]
