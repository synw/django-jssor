# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from jssor.conf import SLIDESHOW_TYPES, BREAKPOINTS


class ResponsiveGroup(models.Model):
    title = models.CharField(max_length=250, verbose_name=_(u'Title'))
    edited = models.DateTimeField(editable=False, auto_now=True, verbose_name=u'Edité le')
    created = models.DateTimeField(editable=False, auto_now_add=True)
    fullscreen = models.BooleanField(default=False, verbose_name=_(u'Fullscreen slideshow'))
    
    class Meta:
        verbose_name = _(u'Responsive groups')
        verbose_name_plural = _(u'Responsive group')

    def __unicode__(self):
        return unicode(self.title)
    
    def save(self, *args, **kwargs):
        slideshows = Slideshow.objects.filter(responsive_group=self)
        for slideshow in slideshows:
            if self.fullscreen is True:
                if not slideshow.fullscreen is True:
                    slideshow.fullscreen = True
                    slideshow.save()
            else:
                if slideshow.fullscreen is True:
                    slideshow.fullscreen = False
                    slideshow.save()
        super(ResponsiveGroup, self).save(*args, **kwargs)


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
    breakpoint = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_(u'Breakpoint'), choices=BREAKPOINTS, default=BREAKPOINTS[0][0])
    responsive_group = models.ForeignKey(ResponsiveGroup, null=True, blank=True, related_name="slideshows", verbose_name=_(u'Responsive group'))
    fullscreen = models.BooleanField(default=False, verbose_name=_(u'Fullscreen slideshow'))
    transitions = models.TextField(blank=True, verbose_name=_(u'Sideshow transitions'))
    captions = models.TextField(blank=True, verbose_name=_(u'Captions transitions'))
    
    class Meta:
        verbose_name = _(u'Slideshow')
        verbose_name_plural = _(u'Slideshows')
        unique_together = ('breakpoint', 'responsive_group')

    def __unicode__(self):
        return unicode(self.title)


class Slide(models.Model):
    title = models.CharField(max_length=250, blank=True, verbose_name=_(u'Title'))
    edited = models.DateTimeField(editable=False, auto_now=True, verbose_name=u'Edité le')
    created = models.DateTimeField(editable=False, auto_now_add=True)
    image = models.ImageField(upload_to='jssor', blank=False, verbose_name=_(u'Image'))
    slideshow = models.ForeignKey(Slideshow, related_name="slides", verbose_name=_(u'Slideshow'))
    order = models.PositiveSmallIntegerField(null=True, verbose_name=_(u'Order'))
    html = models.TextField(blank=True, verbose_name=_(u'Html'), help_text=_(u'For captions or extra html to output'))

    class Meta:
        ordering = ('order', 'slideshow', 'created')
        verbose_name = _(u'Slide')
        verbose_name_plural = _(u'Slides')

    def __unicode__(self):
        return unicode(self.title)
