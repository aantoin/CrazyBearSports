"""Team template tags"""
from django import template

from teams.models import TeamGroup # pylint: disable=import-error

register = template.Library()

@register.simple_tag
def nav_leagues():
    """Get all leagues. Used for base.html nav"""
    return TeamGroup.objects.filter(group_type=TeamGroup.get_group_type_number('league'))

@register.simple_tag
def nav_school_groups():
    """Get all school groups. Used for base.html nav"""
    return TeamGroup.objects.filter(group_type=TeamGroup.get_group_type_number('school'))