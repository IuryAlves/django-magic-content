# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms

from magiccontent.forms import LinkableFormMixin

from .models import LongContent


class LongContentForm(LinkableFormMixin, forms.ModelForm):

    class Meta:
        model = LongContent
        fields = ('title', 'long_content', 'site_link', 'link_label')


class LongContentCreateForm(forms.ModelForm):

    class Meta:
        model = LongContent
        fields = ('title',)
