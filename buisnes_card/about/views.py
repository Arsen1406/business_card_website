from django.shortcuts import render


def about(requests):
    return render(requests, template_name='about/about-me.html')
