# -*- coding: utf-8 -*-
from __future__ import absolute_import

from magiccontent.forms import PictureForm
from magiccontent.widgets import CustomCropImageWidget
from .models import BackgroundArea


class BackgroundAreaForm(PictureForm):

    class Meta:
        model = BackgroundArea
        fields = (
            'title', 'sub_title', 'short_content', 'site_link', 'link_label',
            'picture', 'picture_cropping',)
        widgets = {
            'picture': CustomCropImageWidget(BackgroundArea, 'picture'),
        }
