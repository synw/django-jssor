# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from pages.views import PageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^slideshows/', include('jssor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
urlpatterns.append(url(r'^(?P<url>.*?)$', PageView.as_view()))
