# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


SLIDESHOW_TYPES =   (
                    ('jssor/slideshows/full_width_slider.html', _(u'Full width slider')),
                    ('jssor/slideshows/banner_slider.html', _(u'Banner slider')),
                    ('jssor/slideshows/bootstrap_slider.html', _(u'Bootstrap slider')),
                    ('jssor/slideshows/images_gallery.html', _(u'Images gallery')),
                    ('jssor/slideshows/bootstrap_modal.html', _(u'Bootstrap modal')),
                    )

BREAKPOINTS = (
               (0, _(u'No breakpoint')),
               (320, 'Xxs: 320x480'),
               (360, 'Xs: 360x640'),
               (768, 'Sm: 768x1024')
               )

SLIDESHOW_TYPES = getattr(settings, 'JSSOR_SLIDESHOW_TYPES', SLIDESHOW_TYPES)
BREAKPOINTS = getattr(settings, 'JSSOR_BREAKPOINTS', BREAKPOINTS)


