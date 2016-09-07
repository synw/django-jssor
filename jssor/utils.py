# -*- coding: utf-8 -*-

def encode_ids(slideshows):
    slideshow_ids = 0
    i = 0
    for slideshow in slideshows:
        if i == 0:
            slideshow_ids = str(slideshow.pk)
        else:
            slideshow_ids += '_'+str(slideshow.pk)
        i += 1
    return slideshow_ids