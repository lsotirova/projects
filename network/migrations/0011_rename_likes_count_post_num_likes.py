# Generated by Django 4.1.6 on 2023-03-17 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_rename_num_likes_post_likes_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes_count',
            new_name='num_likes',
        ),
    ]
