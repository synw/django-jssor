# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.flatpages.models import FlatPage
from jssor.models import Slideshow

class Page(FlatPage):
    slideshow = models.ForeignKey(Slideshow, null=True, blank=True, on_delete=models.SET_NULL)