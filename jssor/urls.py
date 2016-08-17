from django.conf.urls import url
from jssor.views import SlideshowDispatcherView

urlpatterns = [
    url(r'^slideshow/(?P<slideshow_ids>[-_\w]+)/(?P<screen_width>[0-9]+)/(?P<screen_height>[0-9]+)/$', SlideshowDispatcherView.as_view(), name="slideshow-dispatcher"),
    ]

