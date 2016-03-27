# -*- coding: utf-8 -*-

from django.conf import settings


SLIDESHOW_TYPES = (
                   ('jssor/full_width_slider.html',_(u'Full width slider')),
                   ('jssor/banner_slider.html',_(u'Banner slider')),
                   ('jssor/bootstrap_slider.html',_(u'Bootstrap slider')),
                   ('jssor/images_slider.html',_(u'Images slider')),
                   )

getattr(settings, 'SLIDESHOW_TYPES', SLIDESHOW_TYPES)
    