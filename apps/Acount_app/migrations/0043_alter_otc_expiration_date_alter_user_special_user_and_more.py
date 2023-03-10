# Generated by Django 4.1 on 2022-09-25 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0042_alter_otc_expiration_date_alter_user_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otc',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 25, 16, 28, 27, 930244, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 25, 16, 23, 27, 914617, tzinfo=datetime.timezone.utc), verbose_name='کاربر خاص تا زمان:'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True, verbose_name='نام کاربری'),
        ),
    ]
