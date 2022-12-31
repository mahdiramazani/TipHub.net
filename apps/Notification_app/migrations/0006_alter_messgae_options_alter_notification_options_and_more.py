# Generated by Django 4.1 on 2022-09-15 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tutorial_app', '0022_alter_category_options_alter_comment_options_and_more'),
        ('Notification_app', '0005_alter_messgae_options_alter_notification_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messgae',
            options={'ordering': ('-created',), 'verbose_name': 'پیام', 'verbose_name_plural': 'پیام ها'},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ('-created',), 'verbose_name': 'اعلان', 'verbose_name_plural': 'اعلانات'},
        ),
        migrations.AlterField(
            model_name='messgae',
            name='body',
            field=models.TextField(verbose_name='متن پیام'),
        ),
        migrations.AlterField(
            model_name='messgae',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='messgae',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال هست یا خیر'),
        ),
        migrations.AlterField(
            model_name='messgae',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to=settings.AUTH_USER_MODEL, verbose_name='ارسال کننده پیام'),
        ),
        migrations.AlterField(
            model_name='messgae',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Message', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='body',
            field=models.TextField(verbose_name='متن اعلان'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification', to='Tutorial_app.videotutorial', verbose_name='فعال هست یا خیر'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification', to=settings.AUTH_USER_MODEL, verbose_name='نام کاربری'),
        ),
    ]
