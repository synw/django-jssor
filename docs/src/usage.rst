Usage
=====

Django Jssor can load different slideshows depending on the screen resolution. The ResponsiveGroup model is
a set of slideshows for different breakpoints. Every slideshow can be thight to a breakpoint. Here
is the models hierarchy:

ResponsiveGroup -> Slideshow -> Slide

How it works: the loader sends an ajax query to the backend, that will render the proper slideshow according
to the device width.

With models
-----------

Create a slideshow and a responsive group. Attach the slideshow to the group. Optionaly add more slideshows
for different breakpoints to the group.

Example with a simple page app:

.. highlight:: python

::

   # models.py
   
   from django.db import models
   from jssor.models import ResponsiveGroup
   
   class Page(models.Model):
      url = models.CharField(max_length=255)
      title = models.CharField(max_length=255)
      content = models.TextField(blank=True)
      slideshow_group = models.ForeignKey(ResponsiveGroup, null=True, blank=True)
    
We need to pass the slideshow group into the template context:

::

   # views.py
   
   from django.views.generic import TemplateView
   from pages.models import Page
   from django.shortcuts import get_object_or_404
   
   class PageView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        url = kwargs['url']
        if not url.startswith('/'):
            url = '/' + url
        if not url.endswith('/'):
            url += '/'
        page = get_object_or_404(Page.objects.prefetch_related("slideshow_group__slideshows"), url=url)
        slideshow_group = page.slideshow_group
        context['page'] = page
        context['slideshows_group'] = slideshow_group
        context['fullscreen'] = slideshow_group.fullscreen
        context['load_jquery'] = True
        return context
        
Include the loader in the template:

::

   # templates/pages/index.html
   
   <html>
   <body>
   {% if not fullscreen %}
   <div id="header">
      Django Jssor Example
   </div>
   {% endif %}
   <div id="slideshow"></div>
   {% include "jssor/loader.html" %}
   <div id="content">
      {% if page.content %}{{ page.content|safe }}{% endif %}
   </div>
   </body>
   </html>

This example is available in the repository.

Standalone
----------

You can display a slideshow from a list of images coming from any ImageField.

.. highlight:: python

::

   # views.py

   obj = MyModel.objects.get(pk=1).select_related("images")
   context["slides"] = obj.images.all()
   
In the template:

.. highlight:: django

::

   {% with 1200 as slideshow_width %}
   {% with 500 as slideshow_height %}
      {% include "jssor/slideshows/bootstrap_slider.html" %}
   {% endwith %}
   {% endwith %} 

