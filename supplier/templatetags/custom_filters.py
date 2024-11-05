# supplier/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.simple_tag
def test_tag():
    return "This is a test."
