# Generated by Django 4.2.1 on 2023-09-12 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_bids_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='title',
        ),
    ]