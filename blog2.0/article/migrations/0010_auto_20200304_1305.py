# Generated by Django 2.1 on 2020-03-04 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_articlepost_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='likes',
            field=models.PositiveIntegerField(default=1136),
        ),
    ]
