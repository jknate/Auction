# Generated by Django 4.2.1 on 2023-09-11 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_bids_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to='auctions.comments'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='current_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='auctions.bids'),
        ),
    ]
