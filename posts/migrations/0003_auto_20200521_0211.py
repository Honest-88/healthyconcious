# Generated by Django 3.0.6 on 2020-05-20 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_baba'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='baba',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slider_post',
        ),
    ]
