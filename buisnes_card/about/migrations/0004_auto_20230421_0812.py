# Generated by Django 2.2.1 on 2023-04-21 08:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20230421_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='year',
        ),
        migrations.AddField(
            model_name='training',
            name='begin',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Начало обучения'),
        ),
        migrations.AddField(
            model_name='training',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Конец обучения'),
        ),
    ]
