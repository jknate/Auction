# Generated by Django 4.2.1 on 2023-09-18 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_listing_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='comments',
        ),
        migrations.AddField(
            model_name='listing',
            name='comments',
            field=models.ManyToManyField(null=True, related_name='comment', to='auctions.comment'),
        ),
    ]
