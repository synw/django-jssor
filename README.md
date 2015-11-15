Jssor slideshows for Django
==============

This application make it easy to use the [jssor](http://jssor.com/) slideshows.

Install
--------------

- Clone the repository
- Get Pillow
- Add 'jssor' to INSTALLED_APPS
- Create the following directories in you media folder: jssor, jssor/thumbnails
- Collect static files
- Run migrations
	
Requirement: a block {% block extra_header %} in the \<head\> tag of the base template to load the javascript

Note: this application is compatible with [django-xadmin](https://github.com/sshwsfc/django-xadmin)

Example usage
--------------

The app's models.py

	from django.db import models
	from django.contrib.flatpages.models import FlatPage
	from jssor.models import Slideshow
	
	class Page(FlatPage):
	    slideshow = models.ForeignKey(Slideshow, related_name='+', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u'Slideshow')
	    
The view:

	from django.conf import settings
	from django.views.generic import TemplateView
	from pages.models import Page
	from jssor.models import Slide
	
	
	class PageView(TemplateView):
	    template_name = 'pages/default.html'
	
	    def get_context_data(self, **kwargs):
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

A basic template:	    

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

Options
--------------

By default the template will not load jquery, asuming that you already did elsewhere. You can change this behavior in the view

	context['load_jquery'] = True

Or directly in the template:

	{% with load_jquery=True %}
		{% include slideshow.template_name %}
	{% endwith %}

By default it loads the necessary jssor js and css files in the {% block extra_header %} of your main template: if you don't want these to be loaded set the variable do_not_load_jssor=True the same way

If you plan to use your own templates you will need this in settings:

	SLIDESHOW_TYPES = (
		('jssor/full_width_slider.html',_(u'Full width slider')),
		('jssor/thumbnails_navigator_with_arrows.html',_(u'Thumbnails navigator with arrows')),
		('jssor/thumbnails_navigator_with_arrows.html',_(u'Banner slider')),
		('jssor/bootstrap_slider.html',_(u'Bootstrap slider')),
		\# Add your templates here
		)

Settings required to run the example
--------------

Add these to INSTALLED_APPS:

	'django.contrib.sites',
	'django.contrib.flatpages'
	'pages',

In the url patterns add: 

	url(r'^(?P<url>.*/)$', PageView.as_view()), 

Contribute
--------------

Fork and add more templates from the [jssor catalog](http://jssor.com/demos/) 

Todo
--------------

- [ ] Use easy_thumbnails for automatic thumbnails generation
