# Generated by Django 2.0.9 on 2018-12-07 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_about_meta_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default=None, upload_to='meta_images'),
            preserve_default=False,
        ),
    ]
