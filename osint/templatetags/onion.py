from django import template

register = template.Library()

@register.filter
def onion(value):
    return value.replace("onion","onion.ly")