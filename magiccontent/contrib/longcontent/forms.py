# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms

from magiccontent.forms import PictureForm, LinkableFormMixin
from magiccontent.widgets import CustomCropImageWidget, RadioImageFilterSelect

from .models import LongContent


class LongContentForm(LinkableFormMixin, PictureForm):

    class Meta:
        model = LongContent
        fields = ('title', 'long_content', 'site_link', 'link_label',
                  'picture', 'picture_cropping', 'picture_filter', )
        widgets = {
            'picture': CustomCropImageWidget(LongContent, 'picture'),
            'picture_filter': RadioImageFilterSelect,
        }


class LongContentCreateForm(forms.ModelForm):

    class Meta:
        model = LongContent
        fields = ('title',)
