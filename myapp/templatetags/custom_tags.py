from django import template

register = template.Library()

@register.filter(name = 'at_index')
def at_index(list, index):
    return list[index]
