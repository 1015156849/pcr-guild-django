# Generated by Django 3.0.6 on 2020-05-20 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200520_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='c70bb32c9aa911eab803d46d6df5224b', max_length=36, primary_key=True, serialize=False),
        ),
    ]
