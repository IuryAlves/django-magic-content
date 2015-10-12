# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms

from magiccontent.forms import LinkableFormMixin

from .models import DividerTextContent


class DividerTextContentForm(LinkableFormMixin, forms.ModelForm):

    class Meta:
        model = DividerTextContent
        fields = ('title', 'sub_title', 'site_link', 'link_label')


class DividerTextContentCreateForm(forms.ModelForm):

    class Meta:
        model = DividerTextContent
        fields = ('title',)
