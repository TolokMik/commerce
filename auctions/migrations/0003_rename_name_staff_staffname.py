# Generated by Django 3.2.9 on 2021-12-16 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_propositions_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='name',
            new_name='staffname',
        ),
    ]
