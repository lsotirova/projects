# Generated by Django 4.1.6 on 2023-03-15 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_post_like_count_alter_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like_count',
        ),
    ]