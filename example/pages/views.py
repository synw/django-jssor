# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from pages.models import Page
from django.shortcuts import get_object_or_404


class PageView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        url = kwargs['url']
        if not url.startswith('/'):
            url = '/' + url
        if not url.endswith('/'):
            url += '/'
        page = get_object_or_404(Page.objects.prefetch_related("slideshow_group__slideshows"), url=url)
        slideshow_group = page.slideshow_group
        context['page'] = page
        context['slideshows_group'] = slideshow_group
        context['fullscreen'] = slideshow_group.fullscreen
        context['load_jquery'] = True
        return context