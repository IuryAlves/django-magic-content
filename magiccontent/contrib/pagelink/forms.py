# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms

from magiccontent.forms import LinkableFormMixin
from .models import PageLink


class PageLinkForm(LinkableFormMixin, forms.ModelForm):

    class Meta:
        model = PageLink
        fields = ('title', 'sub_title', 'site_link', 'link_label')


class PageLinkCreateForm(forms.ModelForm):

    class Meta:
        model = PageLink
        fields = ('title',)
