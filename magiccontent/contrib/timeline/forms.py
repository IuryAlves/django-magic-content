# -*- coding: utf-8 -*-
from __future__ import absolute_import

from floppyforms.widgets import TextInput

# TODO: dependency to NAVIGATION
from navigation.models import SitePage
from magiccontent.forms import PictureForm
from magiccontent.widgets import CustomCropImageWidget, RadioImageFilterSelect

from .models import EntryContent


class EntryContentForm(PictureForm):

    def __init__(self, *args, **kwargs):
        super(EntryContentForm, self).__init__(*args, **kwargs)
        # TODO: Find out a better way to do this
        page_datalist = SitePage.site_objects.links_from_page('/home')
        self.fields['link_url'].widget = TextInput(
            datalist=tuple(page_datalist))

    class Meta:
        model = EntryContent
        fields = ('title', 'entry_author', 'entry_type', 'entry_access',
                  'long_content', 'tags', 'picture', 'picture_cropping',
                  'picture_filter', 'link_url')
        widgets = {
            'picture': CustomCropImageWidget(EntryContent, 'picture'),
            'picture_filter': RadioImageFilterSelect,
        }
