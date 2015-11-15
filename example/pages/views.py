# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from pages.models import Page


class PageView(TemplateView):
    template_name = 'pages/default.html'

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        page=get_object_or_404(Page, slug=self.kwargs['slug']).select_related('slideshow')
        context['page'] = page
        return context