# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models

from image_cropping import ImageRatioField

from magiccontent.abstract_models import BaseContent


class PageLink(BaseContent):

    _widget_type = 'pagelink'

    """ title, subtitle, link1 and picture background """
    picture_cropping = ImageRatioField('picture__picture', '1600x989')
    sub_title = models.CharField(
        _('sub title'), max_length=128, default='', blank=True)

    @classmethod
    def style_list(cls_obj):
        style_list = (
            ('default', 'PageLink - Style 1 (default)'),
            ('button', 'PageLink - Button'), )
        return style_list

    # bellow properties is only to keep de old fields link1_something working
    @property
    def link1_url(self):
        if self.site_link:
            return self.site_link.url
        return ''

    @property
    def link1_label(self):
        return self.link_label
