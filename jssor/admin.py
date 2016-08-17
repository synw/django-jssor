# -*- coding: utf-8 -*-

from django.contrib import admin
from jssor.models import Slideshow, Slide
from jssor.forms import JssorAdminForm
from jssor.conf import USE_ALAPAGE


class SlideInline(admin.StackedInline):
    model = Slide
    extra = 0


@admin.register(Slideshow)
class SlideshowAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    inlines = (SlideInline,)
    ld = ['title', 'template_name', 'width', 'height', 'breakpoint']
    if USE_ALAPAGE:
        ld.append('page')
    list_display = ld
    list_filter = ['template_name', 'created', 'edited']
    search_fields = ['title']
    list_select_related = ['page']


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    form = JssorAdminForm
    date_hierarchy = 'created'
    list_per_page = 10
    list_display = ['title', 'image', 'slideshow', 'order']
    list_filter = ['created', 'edited']
    search_fields = ['title']
