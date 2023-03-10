# Generated by Django 4.1 on 2022-12-05 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0050_alter_otc_expiration_date_alter_user_special_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otc',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 18, 16, 6, 317735, tzinfo=datetime.timezone.utc), verbose_name='تاریخ انقضای کد اعتبار سنجی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 18, 6, 6, 317735, tzinfo=datetime.timezone.utc), verbose_name='کاربر خاص تا زمان:'),
        ),
    ]
