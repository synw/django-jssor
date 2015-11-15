import tempfile
from django.test import TestCase
from jssor.models import Slideshow, Slide

# models test
class SlideshowTest(TestCase):

    def create_slideshow(self, slug="slideshow", template_name="full_width_slider.html", title="Slideshow", width=780, height=300):
        return Slideshow.objects.create(slug=slug, template_name=template_name, title=title, width=width, height=height)

    def test_slideshow_creation(self):
        slideshow = self.create_slideshow()
        self.assertTrue(isinstance(slideshow, Slideshow))
        self.assertEqual(slideshow.template_name, "full_width_slider.html")
        self.assertEqual(slideshow.title, "Slideshow")
        self.assertEqual(slideshow.slug, "slideshow")
        self.assertEqual(slideshow.autoplay, False)
        self.assertEqual(slideshow.width, 780)
        self.assertEqual(slideshow.height, 300)
        self.assertEqual(slideshow.__unicode__(), slideshow.title)
        

class SlideTest(TestCase):
    
    def create_slideshow(self, slug="slideshow", template_name="full_width_slider.html", title="Slideshow", width=780, height=300):
        return Slideshow.objects.create(slug=slug, template_name=template_name, title=title, width=width, height=height)

    def create_slide(self, title='Test slide', order=10, link='/'):
        self.slideshow = self.create_slideshow()
        self.image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        self.thumbnail = tempfile.NamedTemporaryFile(suffix=".jpg").name
        slide = Slide.objects.create(title=title, slideshow=self.slideshow, order=order, link=link, image=self.image, thumbnail=self.thumbnail)
        
        return slide
    
    def test_slide_creation(self):
        slide=self.create_slide()
        self.assertTrue(isinstance(slide, Slide))
        self.assertEqual(slide.title, "Test slide")
        self.assertEqual(slide.__unicode__(), "Test slide ( Slideshow )")
        self.assertEqual(slide.image, self.image)
        self.assertEqual(slide.thumbnail, self.thumbnail)
        self.assertEqual(slide.slideshow, self.slideshow)
        self.assertEqual(slide.order, 10)
        self.assertEqual(slide.link, '/')
        self.assertFalse(slide.link_is_blank)
    
    
