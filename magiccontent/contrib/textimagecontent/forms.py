# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms
from floppyforms.widgets import Textarea

from magiccontent.forms import LinkableFormMixin

from .models import TextImageContent


class TextImageContentForm(LinkableFormMixin, forms.ModelForm):

    class Meta:
        model = TextImageContent
        fields = ('title', 'sub_title', 'short_content',
                  'site_link', 'link_label',)
        widgets = {
            'short_content': Textarea,
        }


class TextImageContentCreateForm(forms.ModelForm):

    class Meta:
        model = TextImageContent
        fields = ('title',)
