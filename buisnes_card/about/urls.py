from django.urls import path
from . import views

urlpatterns = [
    path('', views.about),
    path('skills', views.skills),
    path('training', views.training),
]
