# Generated by Django 2.0.9 on 2018-12-10 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_auto_20181210_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywords',
            name='image',
            field=models.ImageField(default='keyword_meta_images/default.jpg', upload_to='keyword_meta_images'),
        ),
    ]
