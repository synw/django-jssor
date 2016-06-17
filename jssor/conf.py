# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


SLIDESHOW_TYPES =   (
                    ('jssor/full_width_slider.html', _(u'Full width slider')),
                    ('jssor/banner_slider.html', _(u'Banner slider')),
                    ('jssor/bootstrap_slider.html', _(u'Bootstrap slider')),
                    ('jssor/images_slider.html', _(u'Images slider')),
                    ('jssor/bootstrap_modal.html', _(u'Bootstrap modal')),
                    )

BREAKPOINTS = (
               (0, _(u'No breakpoint')),
               (320, 'Xxs: 320x480'),
               (360, 'Xs: 360x640'),
               (768, 'Sm: 768x1024')
               )

SLIDESHOW_TYPES = getattr(settings, 'JSSOR_SLIDESHOW_TYPES', SLIDESHOW_TYPES)
BREAKPOINTS = getattr(settings, 'JSSOR_BREAKPOINTS', BREAKPOINTS)


