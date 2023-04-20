from django.shortcuts import render
from .models import HardSkil, Training


def about(requests):
    template = 'about/about-me.html'
    title = 'Страница обо мне'
    context = {
        'title': title
    }
    return render(requests, template_name=template, context=context)


def skills(requests):
    all_skills = HardSkil.objects.all()
    template = 'about/skills.html'
    title = 'Мои навыки и технологии'
    context = {
        'title': title,
        'all_skills': all_skills
    }
    return render(requests, template_name=template, context=context)
