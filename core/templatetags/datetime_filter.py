from django.utils.timezone import timedelta, datetime
from django import template
from django.utils.timesince import timesince
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter(name="upto")
@stringfilter
def upto(value):
    """
    strip values returned after the comma when using timesince
    return just now instead of 0 minutes
    """
    split_value = value.split(",")[0]
    return split_value
    

upto.is_safe = True

    