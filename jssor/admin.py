# -*- coding: utf-8 -*-

from django.contrib import admin
from jssor.models import Slideshow, Slide


class SlideInline(admin.TabularInline):
    model = Slide
    extra = 0


@admin.register(Slideshow)
class SlideshowAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    inlines = (SlideInline,)
    list_display = ['title', 'template_name']
    list_filter = ['template_name', 'created', 'edited']
    search_fields = ['title']


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_per_page = 10
    list_display = ['title', 'image', 'slideshow', 'order']
    list_filter = ['created', 'edited']
    search_fields = ['title']
