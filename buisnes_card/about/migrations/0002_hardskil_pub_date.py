# Generated by Django 2.2.1 on 2023-04-20 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardskil',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 17, 40, 48, 441207)),
        ),
    ]
