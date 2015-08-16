# -*- coding: utf-8 -*-

from django.db import models
from jssor.models import Slideshow

class Page(models.Model):
    slug = models.SlugField(max_length=150, unique=True)
    content = models.TextField(null=True, blank=True)
    slideshow = models.ForeignKey(Slideshow, null=True, blank=True, on_delete=models.SET_NULL)