Jssor slideshows for Django
==============

[![Build Status](https://travis-ci.org/synw/django-jssor.svg?branch=master)](https://travis-ci.org/synw/django-jssor)

This application make it easy to use the [jssor](http://jssor.com/) slideshows.

Install
--------------

:one: Clone:

  ```bash
cd to_your_project_main_dir
git clone https://github.com/synw/django-jssor.git && mv django-jssor/jssor . && mkdir media/jssor && mkdir media/jssor/thumbnails && rm -rf django-jssor
  ```

:two: Install dependencies:

  ```bash
pip install django-autoslug sorl-thumbnail
  ```

:three: Migrate
		
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
	
- Make sure you `media` folder contains these subfolders: `jssor, jssor/thumbnails`
	
Requirement: a block `{% block extra_header %}` in the \<head\> tag of the base template to load the javascript

Example usage
--------------

Check [the example](example)

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

Developement
--------------

Fork and add more templates from the [jssor catalog](http://jssor.com/demos/) 

You will need this in settings:

  ```python
SLIDESHOW_TYPES = (
	('jssor/full_width_slider.html',_(u'Full width slider')),
	('jssor/thumbnails_navigator_with_arrows.html',_(u'Thumbnails navigator with arrows')),
	('jssor/banner_slider.html',_(u'Banner slider')),
	('jssor/bootstrap_slider.html',_(u'Bootstrap slider')),
	# Add your templates here
	)
  ```

Todo
--------------

- [ ] Add more options to control the slideshow behavior like AutoPlayInterval, ArrowKeyNavigation, JssorBulletNavigator stuff
- [ ] Add more jssor templates and slideshow types
- [x] More tests
- [ ] Editor management
