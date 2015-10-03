import tempfile
from django.test import TestCase
from jssor.models import Slideshow, Slide

# models test
class SlideshowTest(TestCase):

    def create_slideshow(self, slug="slideshow", template_name="full_width_slider.html", title="Slideshow"):
        return Slideshow.objects.create(slug=slug, template_name=template_name, title=title)

    def test_slideshow_creation(self):
        slideshow = self.create_slideshow()
        self.assertTrue(isinstance(slideshow, Slideshow))
        self.assertEqual(slideshow.__unicode__(), slideshow.title)
        self.assertEqual(slideshow.template_name, "full_width_slider.html")
        self.assertEqual(slideshow.title, "Slideshow")
        

class SlideTest(TestCase):
    
    def create_slideshow(self, slug="slideshow", template_name="full_width_slider.html", title="Slideshow"):
        return Slideshow.objects.create(slug=slug, template_name=template_name, title=title)
    
    def create_slide(self, title='Test slide', order=10):
        slideshow = self.create_slideshow()
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        slide = Slide.objects.create(title=title, slideshow=slideshow, order=order, image=image)
        return slide
    
    def test_slide_creation(self):
        slide=self.create_slide()
        self.assertTrue(isinstance(slide, Slide))
        self.assertEqual(slide.title, "Test slide")
        self.assertEqual(slide.__unicode__(), "Test slide ( Slideshow )")
    
    
