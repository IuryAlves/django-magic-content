# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms

from magiccontent.forms import PictureForm, LinkableFormMixin
from magiccontent.widgets import CustomCropImageWidget, RadioImageFilterSelect

from .models import SimpleContent


class SimpleContentForm(LinkableFormMixin, PictureForm):

    class Meta:
        model = SimpleContent
        fields = ('title', 'sub_title', 'short_content',
                  'site_link', 'link_label',
                  'picture', 'picture_cropping', 'picture_filter',)
        widgets = {
            'picture': CustomCropImageWidget(SimpleContent, 'picture'),
            'picture_filter': RadioImageFilterSelect,
        }


class SimpleContentCreateForm(forms.ModelForm):

    class Meta:
        model = SimpleContent
        fields = ('title',)
