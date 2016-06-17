# -*- coding: utf-8 -*-

from django.conf import settings
from django.views.generic import TemplateView
from pages.models import Page
from jssor.models import Slide


class PageView(TemplateView):
    template_name = 'pages/default.html'

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        try:
            url = kwargs['url']
        except:
            url = '/'
        if not url.startswith('/'):
            url = '/' + url
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
        page=Page.objects.filter(url=url)[0]
        context['page'] = page
        context['load_jquery'] = True
        return context