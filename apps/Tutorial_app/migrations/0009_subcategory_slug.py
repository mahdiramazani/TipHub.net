# Generated by Django 4.1 on 2022-08-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial_app', '0008_alter_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True),
        ),
    ]
