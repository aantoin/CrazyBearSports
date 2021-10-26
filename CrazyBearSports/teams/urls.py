"""Team URLs"""
from django.urls import path

from . import views

urlpatterns = [
    path('<slug:group>/', views.team_group_view, name='team_group'),
    path('<slug:group>/<slug:team>', views.team_view, name='team'),
    path('<slug:group>/<slug:team>/edit_inline', views.team_view, kwargs=dict(action='edit_inline'), name='team_content_edit_inline'),
    path('<slug:group>/<slug:team>/edit', views.team_view, kwargs=dict(action='edit'), name='team_content_edit'),
]
