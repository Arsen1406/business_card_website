from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Training(models.Model):
    title = models.CharField(verbose_name='Название курса', max_length=512)
    school = models.CharField(verbose_name='Название школы', max_length=512)
    begin = models.DateTimeField(default=timezone.now, verbose_name='Начало обучения')
    end = models.DateTimeField(default=timezone.now, verbose_name='Конец обучения', blank=True, null=True)
    certificate = models.ImageField(
        verbose_name='Диплом',
        upload_to='static/img',
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-end', ]


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
    course = models.ManyToManyField(Training, verbose_name='Курс')
    pub_date = models.DateTimeField(verbose_name='Дата добавления', default=timezone.now)

    def __str__(self):
        return self.title


class SkillInCourse(models.Model):
    technologies = models.ForeignKey(HardSkil, on_delete=models.CASCADE)
    courses = models.ForeignKey(Training, on_delete=models.CASCADE)