# Generated by Django 4.1.6 on 2023-02-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='start_bid',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]