# Generated by Django 2.0.9 on 2018-12-08 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_sharingmeta_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharingmeta',
            name='text',
        ),
    ]
