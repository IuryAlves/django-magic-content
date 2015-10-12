# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from image_cropping import ImageRatioField

from magiccontent.abstract_models import BaseContent


class FormattedTextImageContent(BaseContent):

    _widget_type = 'formattedtextimagecontent'

    """ title, longtext """
    picture_cropping = ImageRatioField('picture__picture', '960x480')

    def _content(self):
        return self.long_content

    @classmethod
    def style_list(cls_obj):
        style_list = (
            ('default', 'FormattedTextImageContent - List 1 (default)'),
            ('list2', 'FormattedTextImageContent - List 2'),
            ('list3', 'FormattedTextImageContent - List 3'), )
        return style_list
