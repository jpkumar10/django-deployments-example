from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    '''
    This will the values in the string
    '''
    return value.replace(arg, '')

#register('cut', cut)