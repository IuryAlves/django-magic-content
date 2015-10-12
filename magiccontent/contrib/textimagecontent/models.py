# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models

from image_cropping import ImageRatioField

from magiccontent.abstract_models import BaseContent


class TextImageContent(BaseContent):

    _widget_type = 'textimagecontent'

    """ title, subtitle, shorttext """
    sub_title = models.CharField(
        _('sub title'), max_length=128, default='', blank=True)
    picture_cropping = ImageRatioField('picture__picture', '960x593')

    def _content(self):
        return self.short_content

    @classmethod
    def style_list(cls_obj):
        style_list = (
            ('default', 'TextImageContent - List 1 (default)'),
            ('list2', 'TextImageContent - List 2'),
            ('list3', 'TextImageContent - List 3'),
            ('list4', 'TextImageContent - List 4'),
            ('slide_by_1', 'TextImageContent - Slide by 1'), )
        return style_list
