# Generated by Django 3.0.6 on 2020-07-09 04:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_auto_20200708_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 12, 9, 23, 642057)),
        ),
    ]