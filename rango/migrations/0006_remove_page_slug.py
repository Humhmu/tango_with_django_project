# Generated by Django 2.2.28 on 2025-02-09 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20250209_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
