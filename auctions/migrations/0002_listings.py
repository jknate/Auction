# Generated by Django 4.2.1 on 2023-09-11 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image', models.ImageField(upload_to='listing/')),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
