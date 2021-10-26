"""Stats URLs"""
from django.urls import path

from . import views

urlpatterns = [
    path('upload', views.upload, name='stats_upload'),
    path('', views.stats, name='stats'),
]
