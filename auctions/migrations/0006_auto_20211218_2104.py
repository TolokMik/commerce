# Generated by Django 3.2.9 on 2021-12-18 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_staff_startprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='image_one',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='users_photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]