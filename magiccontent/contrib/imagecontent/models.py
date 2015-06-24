# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from image_cropping import ImageRatioField

from magiccontent.abstract_models import BaseContent


class ImageContent(BaseContent):

    _widget_type = 'imagecontent'

    """ title, subtitle"""
    picture_cropping = ImageRatioField('picture__picture', '960x960')

    def _content(self):
        return self.short_content

    def get_absolute_url(self):
        return reverse('flexcontent.imagecontent.update',
                       args=[self.widget.pk, self.pk])

    @classmethod
    def style_list(cls_obj):
        style_list = (
            ('default', 'ImageContent - List'),
            ('caption1', 'ImageContent - Caption 1'),
            ('caption2', 'ImageContent - Caption 2'), )
        return style_list
