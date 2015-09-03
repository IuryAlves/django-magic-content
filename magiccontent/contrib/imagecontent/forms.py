# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms

from magiccontent.forms import LinkableFormMixin

from .models import ImageContent


class ImageContentForm(LinkableFormMixin, forms.ModelForm):

    class Meta:
        model = ImageContent
        fields = ('title', 'short_content', 'site_link', 'link_label')


class ImageContentCreateForm(forms.ModelForm):

    class Meta:
        model = ImageContent
        fields = ('title',)
