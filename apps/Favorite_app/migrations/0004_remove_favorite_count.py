# Generated by Django 4.1 on 2022-12-07 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Favorite_app', '0003_favorite_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='count',
        ),
    ]
