# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import floppyforms.__future__ as forms

from magiccontent.widgets import CustomCropImageWidget, RadioImageFilterSelect
from .models import GalleryContent


class GalleryContentForm(forms.ModelForm):

    class Meta:
        model = GalleryContent
        fields = ('title', 'short_content', 'picture', 'picture_cropping',
                  'picture_filter',)
        widgets = {
            'picture': CustomCropImageWidget(GalleryContent, 'picture'),
            'picture_filter': RadioImageFilterSelect,
        }
