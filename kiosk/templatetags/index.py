from django import template
register = template.Library()


@register.filter
def get_by_id(l, i):
    return l.get(id=i)
