# Generated by Django 4.1 on 2022-08-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial_app', '0003_alter_videotutorial_like_alter_videotutorial_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='videotutorial',
            name='video_cover',
            field=models.ImageField(default=1, upload_to='videotutorial/iamge'),
            preserve_default=False,
        ),
    ]