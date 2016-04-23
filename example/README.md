Jssor slideshows for Django
==============

Example usage
--------------

The app's models.py

  ```python
from django.db import models
from django.contrib.flatpages.models import FlatPage
from jssor.models import Slideshow

class Page(FlatPage):
    slideshow = models.ForeignKey(Slideshow, related_name='+', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u'Slideshow')
  ```

The view.py:

  ```python
from django.conf import settings
from django.views.generic import TemplateView
from pages.models import Page
from jssor.models import Slide


class PageView(TemplateView):
template_name = 'pages/default.html'

def get_context_data(self, **kwargs):
	"""
	Function taken from the original flatpages application
	"""
    context = super(PageView, self).get_context_data(**kwargs)
    try:
        url = kwargs['url']
    except:
        url = '/'
    if not url.startswith('/'):
        url = '/' + url
    if not url.endswith('/') and settings.APPEND_SLASH:
        url += '/'
    page=Page.objects.filter(url=url).select_related('slideshow')[0]
    if page.slideshow:
        context['slideshow'] = page.slideshow
        slides = Slide.objects.filter(slideshow=page.slideshow)
        context['slides'] = slides
    context['page'] = page
    context['load_jquery'] = True
    return context
  ```

A basic template:	 
   
  ```django
<html>
<head>
	<title>{% block title %}{{ page.title }}{% endblock %}</title>
	{% block extra_head %}{% endblock %}
</head>

<body>
{% if slideshow %}
	{% include slideshow.template_name %}
{% endif %}
<h1>{{ page.title }}</h1>
{% if page.content %}{{ page.content|safe }}{% endif %}
</body>
</html>
  ```
For the urls check [urls.py](urls.py)
