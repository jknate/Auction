# Generated by Django 4.2.1 on 2023-09-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_listings_comments_alter_listings_current_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='title',
            field=models.CharField(default='title', max_length=200),
        ),
    ]
