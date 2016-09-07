# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from jssor.models import ResponsiveGroup, Slideshow, Slide
from jssor.forms import JssorAdminForm


class SlideInline(admin.StackedInline):
    model = Slide
    extra = 0


@admin.register(ResponsiveGroup)
class ResponsiveGroupAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ['title', "fullscreen"]
    list_filter = ['created', 'edited']
    search_fields = ['title']


@admin.register(Slideshow)
class SlideshowAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    inlines = (SlideInline,)
    list_display = ['title', 'template_name', 'width', 'height', 'breakpoint']
    list_filter = ['template_name', 'created', 'edited']
    search_fields = ['title']
    
    def get_fieldsets(self, request, obj=None):
        super(SlideshowAdmin, self).get_fieldsets(request, obj)
        fieldsets = (
            (None, {
                'fields': (
                        ('title',),
                        ('width', 'height'),
                        ('template_name', "breakpoint"),
                        ("responsive_group", "fullscreen"),
                        ),
            }),
            (_(u'Slideshow options'), {
                'classes': ('collapse',),
                'fields': (('autoplay','autoplay_interval'), 'bullet_navigator')
            }),
            (_(u'Effects'), {
                'classes': ('collapse',),
                'fields': ('captions', 'transitions')
            }),
        )
        return fieldsets


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    form = JssorAdminForm
    date_hierarchy = 'created'
    list_per_page = 10
    list_display = ['title', 'image', 'slideshow', 'order']
    list_filter = ['created', 'edited']
    search_fields = ['title']
