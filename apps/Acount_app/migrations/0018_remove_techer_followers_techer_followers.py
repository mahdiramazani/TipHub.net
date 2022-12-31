# Generated by Django 4.1 on 2022-08-18 13:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0017_techer_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techer',
            name='followers',
        ),
        migrations.AddField(
            model_name='techer',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]