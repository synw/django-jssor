Jssor slideshows for Django
==============

[![Build Status](https://travis-ci.org/synw/django-jssor.svg?branch=master)](https://travis-ci.org/synw/django-jssor)

This application make it easy to use the [jssor](http://jssor.com/) slideshows.

Install
--------------

Install or clone the latest developpement version:

  ```bash
pip install django-jssor
  ```

  ```bash
cd to_your_project_main_dir
mkdir media/jssor && mkdir media/jssor/thumbnails
  ```

Install dependencies if you cloned the repository:

  ```bash
pip install Pillow sorl-thumbnail
  ```

Migrate
		
  ```bash
python manage.py check
python manage.py makemigrations
python manager.py migrate
  ```

Configuration
--------------

Add 'jssor' to your INSTALLED_APPS

Create `media` folder contains these subfolders: `jssor, jssor/thumbnails`

Requirement: a block `{% block extra_head %}` in the \<head\> tag of the base template to load the 
necessary javascript

Example usage
--------------

Check [the example](example)

Note: for a ready to use implementation in a page management app check [django-alapage](https://github.com/synw/django-alapage)

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

By default it loads the necessary jssor js and css files in the `{% block extra_header %}` of your main template: if you don't want these to be loaded set the variable `do_not_load_jssor=True` the same way

Developement
--------------

Fork and add more templates from the [jssor catalog](http://jssor.com/demos/) 

You will need this in settings:

  ```python
SLIDESHOW_TYPES = (
	('jssor/full_width_slider.html',_(u'Full width slider')),
	('jssor/banner_slider.html',_(u'Banner slider')),
	('jssor/bootstrap_slider.html',_(u'Bootstrap slider')),
	('jssor/images_slider.html',_(u'Images slider')),
	# Add your templates here
	)
  ```

Todo
--------------

- [ ] Add more options to control the slideshow behavior like ArrowKeyNavigation
- [ ] Add more jssor templates and slideshow types
- [ ] More tests

