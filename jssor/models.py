# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from jssor.conf import SLIDESHOW_TYPES


class Slideshow(models.Model):
    title = models.CharField(max_length=250, verbose_name=_(u'Title'))
    edited = models.DateTimeField(editable=False, auto_now=True, verbose_name=u'Edité le')
    created = models.DateTimeField(editable=False, auto_now_add=True)
    template_name = models.CharField(max_length=150, choices=SLIDESHOW_TYPES, default=SLIDESHOW_TYPES[0][0], verbose_name=_(u'Slideshow type'))
    autoplay = models.BooleanField(default=False, verbose_name=_(u'Autoplay'))
    autoplay_interval = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_(u'Autoplay interval'), help_text=_(u'Number of seconds between slides'))
    bullet_navigator = models.BooleanField(default=False, verbose_name=_(u'Bullet navigator'))
    width = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_(u'Width'))
    height = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_(u'Height'))

    class Meta:
        verbose_name = _(u'Slideshow')
        verbose_name_plural = _(u'Slideshows')

    def __unicode__(self):
        return unicode(self.title)


class Slide(models.Model):
    title = models.CharField(max_length=250, blank=True, verbose_name=_(u'Title'))
    edited = models.DateTimeField(editable=False, auto_now=True, verbose_name=u'Edité le')
    created = models.DateTimeField(editable=False, auto_now_add=True)
    image = models.ImageField(upload_to='jssor', blank=False, verbose_name=_(u'Image'))
    slideshow = models.ForeignKey(Slideshow, related_name="slides", verbose_name=_(u'Slideshow'))
    order = models.PositiveSmallIntegerField(null=True, verbose_name=_(u'Order'))
    link = models.CharField(blank=True, max_length=255, verbose_name=_(u'Link'))
    link_is_blank = models.BooleanField(default=False, verbose_name=_(u'Open link in a new tab'))

    class Meta:
        ordering = ('order', 'slideshow', 'created')
        verbose_name = _(u'Slide')
        verbose_name_plural = _(u'Slides')

    def __unicode__(self):
        return unicode(self.title)
