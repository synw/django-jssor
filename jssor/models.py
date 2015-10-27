# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


if hasattr(settings, 'SLIDESHOW_TYPES'):
    SLIDESHOW_TYPES = settings.SLIDESHOW_TYPES
else:
    SLIDESHOW_TYPES = (
                   ('jssor/full_width_slider.html',_(u'Full width slider')),
                   ('jssor/thumbnails_navigator_with_arrows.html',_(u'Thumbnails navigator with arrows')),
                   ('jssor/banner_slider.html',_(u'Banner slider')),
                   ('jssor/bootstrap_slider.html',_(u'Bootstrap slider')),
                   )
    

class Slideshow(models.Model):
    title = models.CharField(max_length=250, null=True, verbose_name=_(u'Title'))
    slug = models.SlugField(max_length=150, unique=True, default='', verbose_name=_(u'Id'), help_text=_(u"This field must not contain any spaces, special characters or capital letter"))
    template_name = models.CharField(max_length=150, null=True, choices=SLIDESHOW_TYPES, default=SLIDESHOW_TYPES[0][0], verbose_name=_(u'Slideshow type'))
    autoplay = models.BooleanField(default=False, verbose_name=_(u'Autoplay'))
    width = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_(u'Width'))
    height = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_(u'Height'))

    class Meta:
        verbose_name = _(u'Slideshow')
        verbose_name_plural = _(u'Slideshows')

    def __unicode__(self):
        return unicode(self.title)
    
    
class Slide(models.Model):
    title = models.CharField(max_length=250, null=True, verbose_name=_(u'Title'))
    image = models.ImageField(upload_to='jssor', blank=False, null=True, verbose_name=_(u'Image'))
    thumbnail = models.ImageField(upload_to='jssor/thumbnails', blank=True, null=True, verbose_name=_(u'Thumbnail'))
    slideshow = models.ForeignKey(Slideshow, null=True, on_delete=models.SET_NULL, verbose_name=_(u'Slideshow'))
    order = models.PositiveSmallIntegerField(null=True, verbose_name=_(u'Order'))
    link = models.CharField(null=True, blank=True, max_length=255, verbose_name=_(u'Link'))
    link_is_blank = models.BooleanField(default=False, verbose_name=_(u'Open link in a new tab'))
    
    class Meta:
        ordering = ('order',)
        verbose_name=_(u'Slide')
        verbose_name_plural = _(u'Slides')

    def __unicode__(self):
        if self.slideshow:
            return unicode(self.title)+' ( '+self.slideshow.title+' )'
        else:
            return unicode(self.title)+_(u' ( No slideshow )')
    
    
    