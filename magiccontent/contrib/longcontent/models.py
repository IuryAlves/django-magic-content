# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from image_cropping import ImageRatioField

from magiccontent.abstract_models import BaseContent


class LongContent(BaseContent):

    _widget_type = 'longcontent'

    """ title, longtext """
    picture_cropping = ImageRatioField('picture__picture', '960x480')

    def _content(self):
        return self.long_content

    @classmethod
    def style_list(cls_obj):
        style_list = (
            ('default', 'LongContent - List 1 (default)'),
            ('list2', 'LongContent - List 2'),
            ('list3', 'LongContent - List 3'), )
        return style_list
