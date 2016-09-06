# -*- coding: utf-8 -*-

from django.db import models
from jssor.models import ResponsiveGroup

class Page(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slideshow_group = models.ForeignKey(ResponsiveGroup, null=True, blank=True)
    
    def __unicode__(self):
        return self.title+" "+self.url