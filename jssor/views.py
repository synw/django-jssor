# -*- coding: utf-8 -*-

from django.conf import settings
from django.views.generic import TemplateView
from django.http import Http404, HttpResponse
from jssor.models import Slideshow


class SlideshowDispatcherView(TemplateView):
    
    def get_context_data(self, **kwargs):
        context = super(SlideshowDispatcherView, self).get_context_data(**kwargs)
        if self.request.is_ajax():
            try:
                slideshows = Slideshow.objects.filter(group_id=kwargs['group_id']).prefetch_related('slides')
                screen_width = int(kwargs['screen_width'])
                screen_height = int(kwargs['screen_height'])
            except:
                return context
            # find the slideshow according to the screen size
            slideshow = slideshows.filter(breakpoint=0)[0]
            if screen_width <= 320:
                slideshow = slideshows.filter(breakpoint=320)[0]
            elif screen_width <= 360:
                slideshow = slideshows.filter(breakpoint=360)[0]
            elif screen_width <= 769:
                slideshow = slideshows.filter(breakpoint=768)[0]
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




