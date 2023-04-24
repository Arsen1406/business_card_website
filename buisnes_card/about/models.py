from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Carrier(models.Model):
    post = models.CharField(
        max_length=512,
        verbose_name='Должность'
    )
    company = models.CharField(
        max_length=512,
        verbose_name='Компания',
    )
    duties = models.TextField(
        max_length=1024,
        verbose_name='Должностные обязанности',
    )
    achievements = models.TextField(
        max_length=1024,
        verbose_name='Достижения',
    )

    start_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Начало работы'
    )
    end_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Завершение работы',
        blank=True, null=True
    )

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'


class Training(models.Model):
    title = models.CharField(verbose_name='Название курса', max_length=512)
    school = models.CharField(verbose_name='Название школы', max_length=512)
    begin = models.DateTimeField(
        default=timezone.now,
        verbose_name='Начало обучения'
    )
    end = models.DateTimeField(
        default=timezone.now,
        verbose_name='Конец обучения',
        blank=True, null=True
    )
    certificate = models.ImageField(
        verbose_name='Диплом',
        upload_to='static/img',
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обучение'
        verbose_name_plural = 'Обучение'
        ordering = ['-end', ]


class HardSkil(models.Model):
    title = models.CharField(
        verbose_name='Название технологии',
        max_length=255
    )
    description = models.CharField(
        verbose_name='Описание технологии',
        max_length=1024, null=True
    )
    mastered = models.IntegerField(
        verbose_name='Степень освоения',
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    carriers = models.ManyToManyField(
        Carrier,
        related_name='carrier',
        verbose_name='Работа'
    )
    course = models.ManyToManyField(
        Training,
        related_name='course',
        verbose_name='Курс'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата добавления',
        default=timezone.now
    )
    icon = models.ImageField(
        verbose_name='Иконка технологии',
        upload_to='static/img',
        blank=True,
        null=True
    )
    color = models.CharField(
        verbose_name='color',
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Технологии'
        verbose_name_plural = 'Технологии'
