# -*- coding: utf-8 -*-

from django.contrib import admin
from jssor.models import Slideshow, Slide
from jssor.forms import JssorAdminForm


class SlideInline(admin.StackedInline):
    model = Slide
    extra = 0


@admin.register(Slideshow)
class SlideshowAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    inlines = (SlideInline,)
    list_display = ['title', 'template_name', 'width', 'height', 'breakpoint', 'group_id']
    list_filter = ['template_name', 'created', 'edited']
    search_fields = ['title']


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    form = JssorAdminForm
    date_hierarchy = 'created'
    list_per_page = 10
    list_display = ['title', 'image', 'slideshow', 'order']
    list_filter = ['created', 'edited']
    search_fields = ['title']
