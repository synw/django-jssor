# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.http import Http404
from django.conf import settings
from jssor.models import Slideshow


def decode_slideshow_ids(encoded_ids):
    slideshow_ids = []
    if '_' in encoded_ids:
        for sid in encoded_ids.split("_"):
            slideshow_ids.append(int(sid))
    else:
        slideshow_ids = [int(encoded_ids)]
    return slideshow_ids


class SlideshowDispatcherView(TemplateView):
    
    def get_context_data(self, **kwargs):
        context = super(SlideshowDispatcherView, self).get_context_data(**kwargs)
        if self.request.is_ajax():
            try:
                slideshow_ids = decode_slideshow_ids(kwargs['slideshow_ids'])
                slideshows = Slideshow.objects.filter(pk__in=slideshow_ids).prefetch_related('slides').order_by("breakpoint")
                screen_width = int(kwargs['screen_width'])
                screen_height = int(kwargs['screen_height'])
            except:
                return context
            # find the slideshow according to the screen size
            slideshow = slideshows[0]
            if screen_width <= 320:
                print "320"
                try:
                    slideshow = slideshows.filter(breakpoint=320)[0]
                except:
                    pass
            elif screen_width <= 360:
                print "360"
                try:
                    slideshow = slideshows.filter(breakpoint=360)[0]
                except:
                    pass
            elif screen_width <= 769:
                print "769"
                try:
                    slideshow = slideshows.filter(breakpoint=768)[0]
                except:
                    pass
            
            #print str(slideshow)+' / '+str(screen_width)+'x'+str(screen_height)
            context['slideshow'] = slideshow
            context['slides'] = slideshow.slides.all()
            self.slideshow = slideshow
            if settings.DEBUG:
                context['screen_width'] = screen_width
                context['screen_height'] = screen_height
        else:
            raise Http404
        return context
    
    def get_template_names(self):
        return self.slideshow.template_name




