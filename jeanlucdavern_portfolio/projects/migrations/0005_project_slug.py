# Generated by Django 2.0.9 on 2018-11-20 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20181120_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='test-test'),
            preserve_default=False,
        ),
    ]