from django.utils.http import urlencode
from django import template

from goods.models import Categories

register = template.Library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.ipdate(kwargs)
    return urlencode(query)