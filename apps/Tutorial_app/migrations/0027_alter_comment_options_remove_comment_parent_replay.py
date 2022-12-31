# Generated by Django 4.1 on 2022-12-10 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial_app', '0026_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',), 'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='Tutorial_app.comment')),
            ],
        ),
    ]
