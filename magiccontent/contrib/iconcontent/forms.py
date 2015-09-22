# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms
from floppyforms.widgets import Textarea

from magiccontent.widgets import RadioIconSelect
from magiccontent.forms import LinkableFormMixin

from .models import IconContent


class IconContentForm(LinkableFormMixin, forms.ModelForm):

    class Meta:
        model = IconContent
        fields = ('title', 'short_content', 'icon', 'site_link', 'link_label',)
        widgets = {
            'icon': RadioIconSelect,
            'short_content': Textarea,
        }


class IconContentCreateForm(forms.ModelForm):

    class Meta:
        model = IconContent
        fields = ('title',)
