# Generated by Django 4.1 on 2022-08-28 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0022_user_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
    ]
