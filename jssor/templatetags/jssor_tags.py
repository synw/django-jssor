# -*- coding: utf-8 -*-

from django import template
from jssor.utils import encode_ids


register = template.Library()

@register.simple_tag
def ids_from_group(responsive_group):
    slideshow_ids = ""
    if responsive_group:
        slideshow_ids = encode_ids(responsive_group.slideshows.all())
    return slideshow_ids
        