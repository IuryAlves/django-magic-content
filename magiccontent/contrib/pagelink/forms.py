# -*- coding: utf-8 -*-
from __future__ import absolute_import

# TODO: fix core dependency
from core.helpers import LinkListForm

from magiccontent.forms import PictureForm
from .models import PageLink
from .widgets import CustomCropImageWidget


class PageLinkForm(LinkListForm, PictureForm):

    show_links_on_field = 'link1_url'

    class Meta:
        model = PageLink
        fields = ('title', 'sub_title', 'link1_url',
                  'link1_label', 'picture', 'picture_cropping',)
        widgets = {
            'picture': CustomCropImageWidget(PageLink, 'picture'),
        }
