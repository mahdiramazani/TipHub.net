# Generated by Django 4.1 on 2022-12-07 00:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0060_alter_otc_expiration_date_alter_user_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otc',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 7, 0, 44, 6, 945342, tzinfo=datetime.timezone.utc), verbose_name='تاریخ انقضای کد اعتبار سنجی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 7, 0, 34, 6, 943832, tzinfo=datetime.timezone.utc), verbose_name='کاربر خاص تا زمان:'),
        ),
    ]
