# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms

from magiccontent.forms import LinkableFormMixin

from .models import FormattedTextImageContent


class FormattedTextImageContentForm(LinkableFormMixin, forms.ModelForm):

    class Meta:
        model = FormattedTextImageContent
        fields = ('title', 'long_content', 'site_link', 'link_label')


class FormattedTextImageContentCreateForm(forms.ModelForm):

    class Meta:
        model = FormattedTextImageContent
        fields = ('title',)
