# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.flatpages.models import FlatPage
from jssor.models import Slideshow

class Page(FlatPage):
    slideshow_group = models.SlugField(null=True, blank=True, verbose_name=_(u'Slideshows group id'))