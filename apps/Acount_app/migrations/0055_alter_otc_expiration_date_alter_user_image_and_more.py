# Generated by Django 4.1 on 2022-12-06 22:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0054_alter_otc_expiration_date_alter_user_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otc',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 22, 15, 9, 390287, tzinfo=datetime.timezone.utc), verbose_name='تاریخ انقضای کد اعتبار سنجی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(blank=True, default='media/defult/index.jpg', null=True, upload_to='user/image', verbose_name='تصویر پروفایل'),
        ),
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 22, 5, 9, 390287, tzinfo=datetime.timezone.utc), verbose_name='کاربر خاص تا زمان:'),
        ),
    ]