# Generated by Django 2.0.9 on 2018-12-07 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_about_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='meta_description',
            field=models.CharField(default='default_meta_description_string', max_length=160),
            preserve_default=False,
        ),
    ]