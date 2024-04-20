from django import template

register = template.Library()

@register.filter
def calculate_delay(counter):
    return counter * 0.1 + 0.4
