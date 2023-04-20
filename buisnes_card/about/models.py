import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class HardSkil(models.Model):
    title = models.CharField(verbose_name='Название технологии', max_length=255)
    description = models.CharField(verbose_name='Описание технологии', max_length=1024, null=True)
    mastered = models.IntegerField(
        verbose_name='Степень освоения',
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    pub_date = models.DateTimeField(default=datetime.datetime.now())


class Training(models.Model):
    title = models.CharField(verbose_name='Название курса', max_length=512)
    school = models.CharField(verbose_name='Название школы', max_length=512)
    year = models.CharField(verbose_name='Время обучения', max_length=512)
    certificate = models.ImageField(
        verbose_name='Диплом',
        upload_to='training/',
        blank=True
    )
