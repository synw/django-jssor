Jssor slideshows for Django
==============

[![Build Status](https://travis-ci.org/synw/django-jssor.svg?branch=master)](https://travis-ci.org/synw/django-jssor)

This application make it easy to use the [jssor](http://jssor.com/) slideshows.

Install
--------------

1. Clone:

  ```bash
cd to_your_project_main_dir
git clone https://github.com/synw/django-jssor.git && mv django-jssor/jssor . && mkdir media && mkdir media/jssor && mkdir media/jssor/thumbnails && rm -rf django-jssor
  ```

2. Install dependencies:

  ```bash
pip install django-autoslug sorl-thumbnail
  ```

3. Migrate
		
  ```bash
python manage.py check
python manage.py makemigrations
python manager.py migrate
  ```

Configuration
--------------

- Make sure your INSTALLED_APPS contains the following:

		'django.contrib.sites',
		'django.contrib.flatpages'
		'django-autoslug',
		'sorl.thumbnail',
		'jssor',
	
- Create the following directories in you media folder: `jssor, jssor/thumbnails`
	
Requirement: a block `{% block extra_header %}` in the \<head\> tag of the base template to load the javascript

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
	{% block extra_header %}{% endblock %}
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

For a ready to use implementation check [django-alapage](https://github.com/synw/django-alapage)

Options
--------------

By default the template will not load jquery, asuming that you already did elsewhere. You can change this behavior in the view

  ```python
context['load_jquery'] = True
  ```

Or directly in the template:

  ```django
{% with load_jquery=True %}
	{% include slideshow.template_name %}
{% endwith %}
  ```

By default it loads the necessary jssor js and css files in the {% block extra_header %} of your main template: if you don't want these to be loaded set the variable do_not_load_jssor=True the same way

Settings required to run the example
--------------

Add these to INSTALLED_APPS:

	'django.contrib.sites',
	'django.contrib.flatpages'
	'pages',

And in settings.py:

	SITE_ID = 1

For the urls check urls.py in the example

Developement
--------------

Fork and add more templates from the [jssor catalog](http://jssor.com/demos/) 

You will need this in settings:

	SLIDESHOW_TYPES = (
		('jssor/full_width_slider.html',_(u'Full width slider')),
		('jssor/thumbnails_navigator_with_arrows.html',_(u'Thumbnails navigator with arrows')),
		('jssor/banner_slider.html',_(u'Banner slider')),
		('jssor/bootstrap_slider.html',_(u'Bootstrap slider')),
		# Add your templates here
		)

Todo
--------------

- [ ] Add more options to control the slideshow behavior like AutoPlayInterval, ArrowKeyNavigation, JssorBulletNavigator stuff
- [ ] Add more jssor templates and slideshow types
- [x] More tests
- [ ] Editor management
