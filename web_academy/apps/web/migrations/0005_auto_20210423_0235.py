# Generated by Django 3.1.7 on 2021-04-23 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20210423_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testrequest',
            name='test_type',
            field=models.CharField(choices=[('teorico', 'Teórico'), ('practico', 'Práctico')], max_length=10),
        ),
    ]
