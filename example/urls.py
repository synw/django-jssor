from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from pages.views import PageView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<slug>[-\w]+)/$', PageView.as_view()),
]