# Generated by Django 2.1 on 2020-03-04 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20200304_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
