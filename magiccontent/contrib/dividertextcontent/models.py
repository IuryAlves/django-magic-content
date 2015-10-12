# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models

from image_cropping import ImageRatioField

from magiccontent.abstract_models import BaseContent


class DividerTextContent(BaseContent):

    _widget_type = 'dividertextcontent'

    """ title, subtitle, link1 and picture background """
    picture_cropping = ImageRatioField('picture__picture', '1600x989')
    sub_title = models.CharField(
        _('sub title'), max_length=128, default='', blank=True)

    @classmethod
    def style_list(cls_obj):
        style_list = (
            ('default', 'DividerTextContent - Style 1 (default)'),
            ('button', 'DividerTextContent - Button'), )
        return style_list

    @classmethod
    def can_edit_description(cls_obj):
        return False
