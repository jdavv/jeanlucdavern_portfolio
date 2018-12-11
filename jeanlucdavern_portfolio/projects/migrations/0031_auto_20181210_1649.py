# Generated by Django 2.0.9 on 2018-12-10 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0030_auto_20181210_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='keywords',
            name='description',
            field=models.CharField(default='default', max_length=168),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='keywords',
            name='image',
            field=models.ImageField(default='keyword_meta_images/default.jpg', upload_to='keyword_meta_images'),
        ),
        migrations.AddField(
            model_name='keywords',
            name='title',
            field=models.CharField(default='default', max_length=60),
            preserve_default=False,
        ),
    ]
