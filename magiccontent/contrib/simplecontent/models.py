# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models

from image_cropping import ImageRatioField

from magiccontent.abstract_models import BaseContent


class SimpleContent(BaseContent):

    _widget_type = 'simplecontent'

    """ title, subtitle, shorttext """
    sub_title = models.CharField(
        _('sub title'), max_length=128, default='', blank=True)
    picture_cropping = ImageRatioField('picture__picture', '960x593')

    def _content(self):
        return self.short_content
