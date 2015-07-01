# -*- coding: utf-8 -*-
from __future__ import absolute_import

from magiccontent.forms import PictureForm
from magiccontent.widgets import CustomCropImageWidget, RadioImageFilterSelect

from .models import ImageContent


class ImageContentForm(PictureForm):

    class Meta:
        model = ImageContent
        fields = ('title', 'short_content', 'picture', 'picture_cropping',
                  'picture_filter', 'site_link')
        widgets = {
            'picture': CustomCropImageWidget(ImageContent, 'picture'),
            'picture_filter': RadioImageFilterSelect,
        }
