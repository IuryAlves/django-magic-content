# -*- coding: utf-8 -*-
from __future__ import absolute_import

from floppyforms.widgets import TextInput

# TODO: dependency to NAVIGATION
from navigation.models import SitePage

from magiccontent.forms import PictureForm
from magiccontent.widgets import CustomCropImageWidget
from .models import BackgroundArea


class BackgroundAreaForm(PictureForm):

    def __init__(self, *args, **kwargs):
        super(BackgroundAreaForm, self).__init__(*args, **kwargs)
        # TODO: Find out a better way to do this
        page_datalist = SitePage.site_objects.links_from_page('/home')
        self.fields['link1_url'].widget = TextInput(
            datalist=tuple(page_datalist))

    class Meta:
        model = BackgroundArea
        fields = (
            'title', 'sub_title', 'short_content', 'link1_url', 'link1_label',
            'picture', 'picture_cropping',)
        widgets = {
            'picture': CustomCropImageWidget(BackgroundArea, 'picture'),
        }
