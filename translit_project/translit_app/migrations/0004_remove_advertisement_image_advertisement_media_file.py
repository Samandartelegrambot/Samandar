# Generated by Django 5.1.7 on 2025-03-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translit_app', '0003_advertisement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='image',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='media_file',
            field=models.FileField(blank=True, null=True, upload_to='ads/'),
        ),
    ]
