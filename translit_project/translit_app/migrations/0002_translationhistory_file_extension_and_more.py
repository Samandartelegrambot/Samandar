# Generated by Django 5.1.7 on 2025-03-08 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translit_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='translationhistory',
            name='file_extension',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='translationhistory',
            name='direction',
            field=models.CharField(max_length=20),
        ),
    ]
