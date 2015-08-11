# -*- coding: utf-8 -*-
from __future__ import absolute_import

from magiccontent.forms import PictureForm, LinkableFormMixin
from magiccontent.widgets import CustomCropImageWidget
from .models import PageLink


class PageLinkForm(LinkableFormMixin, PictureForm):

    class Meta:
        model = PageLink
        fields = ('title', 'sub_title', 'site_link',
                  'link_label', 'picture', 'picture_cropping',)
        widgets = {
            'picture': CustomCropImageWidget(PageLink, 'picture'),
        }
