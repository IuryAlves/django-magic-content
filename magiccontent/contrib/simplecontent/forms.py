# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms
from floppyforms.widgets import Textarea

from magiccontent.forms import LinkableFormMixin

from .models import SimpleContent


class SimpleContentForm(LinkableFormMixin, forms.ModelForm):

    class Meta:
        model = SimpleContent
        fields = ('title', 'sub_title', 'short_content',
                  'site_link', 'link_label',)
        widgets = {
            'short_content': Textarea,
        }


class SimpleContentCreateForm(forms.ModelForm):

    class Meta:
        model = SimpleContent
        fields = ('title',)
