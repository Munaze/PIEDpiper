# Generated by Django 2.1.5 on 2019-01-19 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='grnre',
            new_name='genre',
        ),
    ]
