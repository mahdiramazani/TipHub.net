# Generated by Django 4.1 on 2022-10-01 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial_app', '0023_alter_videotutorial_video_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
    ]
