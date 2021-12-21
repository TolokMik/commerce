# Generated by Django 3.2.9 on 2021-12-20 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_staff_image_one'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_descript',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staff',
            name='image_one',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='staff',
            name='startprice',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
