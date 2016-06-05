import functools

from django import template

register = template.Library()

@register.filter(name='key')
def key(d, key_name):
    return d[key_name]

sentinel = object()
@register.filter(name='getattribute')
def getattribute(obj, attr, default=sentinel):
    if default is sentinel:
        _getattr = getattr
    else:
        def _getattr(obj, name):
            return getattr(obj, name, default)
    return functools.reduce(_getattr, [obj]+attr.split('.'))

@register.filter(name='sizeof_fmt')
def sizeof_fmt(num, suffix='B'):
    # num = float(num)
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)