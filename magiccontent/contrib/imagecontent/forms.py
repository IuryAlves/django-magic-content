# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms

from magiccontent.forms import PictureForm, LinkableFormMixin
from magiccontent.widgets import CustomCropImageWidget, RadioImageFilterSelect

from .models import ImageContent


class ImageContentForm(LinkableFormMixin, PictureForm):

    class Meta:
        model = ImageContent
        fields = ('title', 'short_content', 'site_link', 'link_label',
                  'picture', 'picture_cropping', 'picture_filter', )
        widgets = {
            'picture': CustomCropImageWidget(ImageContent, 'picture'),
            'picture_filter': RadioImageFilterSelect,
        }


class ImageContentCreateForm(forms.ModelForm):

    class Meta:
        model = ImageContent
        fields = ('title',)
