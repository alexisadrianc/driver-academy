# Generated by Django 3.1.7 on 2021-04-22 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
