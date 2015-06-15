# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models

from image_cropping import ImageRatioField

from magiccontent.abstract_models import BaseContent


class BackgroundArea(BaseContent):

    _widget_type = 'background'

    """ title, subtitle"""
    picture_cropping = ImageRatioField('picture__picture', '1600x952')
    sub_title = models.CharField(
        _('sub title'), max_length=128, default='', blank=True)
    link1_url = models.CharField(
        _('link1 url'), max_length=255, null=True, blank=True,
        default='#intro')
    link1_label = models.CharField(
        _('link1 label'), max_length=64, default='link1', blank=True)

    def _content(self):
        return self.short_content

    @classmethod
    def style_list(cls_obj):
        style_list = (
            ('default', 'Background - Style 1 (default)'),
            ('style2', 'Background - Style 2 - long'),
            ('style3', 'Background - Style 3 - small'),
            ('bg-slider1', 'Background - Slider 1'),
            ('style4', 'Background - Style 4 - half'), )
        return style_list
