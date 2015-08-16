# -*- coding: utf-8 -*-

from django.views.generic.detail import DetailView
from pages.models import Page


class PageView(DetailView):
    template_name = 'pages/default.html'
    model = Page