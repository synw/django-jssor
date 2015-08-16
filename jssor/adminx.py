# -*- coding: utf-8 -*-

from django.conf import settings
from jssor.models import Slideshow, Slide
try:
    import xadmin

    class SlideXadmin(object):
        if 'reversion' in settings.INSTALLED_APPS:
            reversion_enable = True
        show_bookmarks = False
        list_display = ['title','image','slideshow']
    
    
    class SlideshowXadmin(object):
        if 'reversion' in settings.INSTALLED_APPS:
            reversion_enable = True
        show_bookmarks = False
        relfield_style = 'fk-ajax'
    
    
    xadmin.site.register(Slide, SlideXadmin)
    xadmin.site.register(Slideshow, SlideshowXadmin)
except:
    pass