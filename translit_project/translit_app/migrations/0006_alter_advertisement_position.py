# Generated by Django 5.1.7 on 2025-03-08 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translit_app', '0005_advertisement_position_advertisement_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='position',
            field=models.CharField(choices=[('sidebar', 'Yon panel'), ('top', 'Tepa'), ('popup', 'Popup'), ('interstitial', 'Interstitial')], default='sidebar', max_length=15),
        ),
    ]
