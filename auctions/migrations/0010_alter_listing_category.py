# Generated by Django 4.1.6 on 2023-02-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_rename_comment_date_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('', ''), ('Books', 'Books'), ('Music', 'Music'), ('Beauty', 'Beauty'), ('Sport', 'Sport'), ('Electronics', 'Electronics'), ('Other', 'Other')], default='', max_length=15),
        ),
    ]
