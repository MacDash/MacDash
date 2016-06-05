import functools
import math

from datetime import datetime

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


@register.filter(name='mult')
def mult(value, arg):
    "Multiplies the arg and the value"
    return int(value) * int(arg)


@register.filter(name='sub')
def sub(value, arg):
    "Subtracts the arg from the value"
    return int(value) - int(arg)


@register.filter(name='div')
def div(value, arg):
    "Divides the value by the arg"
    return int(value) / int(arg)


@register.filter(name='floor')
def floor(value):
    return math.floor(value)


@register.filter(name='dayssince')
def dayssince(date):
    date_diff = datetime.now(tz=date.tzinfo) - date
    if date_diff.days == 0:
        return 'Today'
    elif date_diff.days == 1:
        return '{} Day'.format(date_diff.days)
    else:
        return '{} Days'.format(date_diff.days)
