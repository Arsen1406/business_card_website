from datetime import timedelta
from django.shortcuts import render
from .models import HardSkil, Training


def delta_time(begin, end):
    delt = timedelta(begin, end)
    if delt.days >= 365:
        duration = delt.days / 30
        duration = delt.days / 12
        return duration
    return f'{delt.days / 30} месяцев.'


def about(requests):
    template = 'about/about-me.html'
    title = 'Об Авторе'
    context = {
        'title': title
    }
    return render(requests, template_name=template, context=context)


def skills(requests):
    all_skills = HardSkil.objects.prefetch_related('course').all()
    template = 'about/skills.html'
    title = 'Навыки и технологии'
    context = {
        'title': title,
        'all_skills': all_skills
    }
    return render(requests, template_name=template, context=context)


def training(requests):
    all_training = Training.objects.all()
    template = 'about/training.html'
    title = 'Образование'
    context = {
        'title': title,
        'all_training': all_training
    }
    return render(requests, template_name=template, context=context)
