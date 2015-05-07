# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from image_cropping import ImageRatioField

from magiccontent.models import BaseContent


class GalleryContent(BaseContent):

    _widget_type = 'gallerycontent'

    """ title, subtitle"""
    picture_cropping = ImageRatioField('picture__picture', '960x960')

    def _content(self):
        return self.short_content
