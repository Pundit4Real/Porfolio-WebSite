from django import template

register = template.Library()

@register.filter
def calculate_delay_resume(counter):
    return counter * 0.1 + 0.4

@register.filter
def skills(counter):
    return counter * 0.1 + 0.3
