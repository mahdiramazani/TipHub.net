# Generated by Django 4.1 on 2022-08-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial_app', '0010_remove_videotutorial_like_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videotutorial',
            name='video_cover',
            field=models.FileField(upload_to='videotutorial/iamge'),
        ),
    ]