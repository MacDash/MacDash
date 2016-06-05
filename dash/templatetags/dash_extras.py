import functools

from django import template

register = template.Library()

@register.filter(name='key')
def key(d, key_name):
    return d[key_name]

@register.filter(name='getattribute')
def getattribute(obj, attr):
    return functools.reduce(getattr, [obj]+attr.split('.'))

@register.filter(name='sizeof_fmt')
def sizeof_fmt(num, suffix='B'):
    num = float(num)
    for unit in ['M', 'G']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)