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
- If you plan to use your own templates you will need this in settings:

	SLIDESHOW_TYPES = (('jssor/full_width_slider.html',_(u'Full width slider')),
		('jssor/thumbnails_navigator_with_arrows.html',_(u'Thumbnails navigator with arrows')),
		('jssor/thumbnails_navigator_with_arrows.html',_(u'Banner slider')),
		\# Add your templates here
		)
	
Requirement: a block {% block extra_header %} in the \<head\> tag of the base template to load the javascript

Note: this application is compatible with [django-xadmin](https://github.com/sshwsfc/django-xadmin)

Example usage
--------------

Your app's models.py

	from django.db import models
	from django.contrib.flatpages.models import FlatPage
	from jssor.models import Slideshow
	
	class Page(FlatPage):
	    slideshow = models.ForeignKey(Slideshow, related_name='+', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u'Slideshow')
	    slideshow_bottom = models.ForeignKey(Slideshow, related_name='+', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u'Slideshow bottom')
	    
Your template:	    
	    
	{% extends "base.html" %}
	
	{% block title %}{{ flatpage.title }}{% endblock %}
	
	{% block content %}
		{% if flatpage.slideshow %}
		{% with flatpage.slideshow.slides.all as slides %}
			{# I already have jquery loaded somewhere else so I don't want it to be loaded here #}
			{% with load_jquery=0 %}
				{% include flatpage.slideshow.template_name %}
			{% endwith %}
		{% endwith %}
		{% endif %}
		{% if flatpage.content %}{{ flatpage.content|safe }}{% endif %}
		{% if flatpage.slideshow_bottom %}
			<div>
				{% with flatpage.slideshow_bottom.slides.all as slides %}
					{# Prevent jssor and jquery from being loaded twice #}
					{% if flatpage.slideshow %}
						{% with load_jssor=0 load_jquery=0 %}
							{% include flatpage.slideshow_bottom.template_name %}
						{% endwith %}
					{% else %}
						{% with load_jquery=0 %}
							{% include flatpage.slideshow_bottom.template_name %}
						{% endwith %}
					{% endif %}
				{% endwith %}
			</div>
		{% endif %}
	{% endblock %}
	    
Contribute
--------------

Fork and add more templates from the [jssor catalog](http://jssor.com/demos/) 
