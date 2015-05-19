# -*- coding: utf-8 -*-
from __future__ import absolute_import

from floppyforms.widgets import TextInput

# TODO: dependency to NAVIGATION
from navigation.models import SitePage

from magiccontent.forms import PictureForm
from magiccontent.widgets import CustomCropImageWidget
from .models import SimpleContent

# TODO: dependency to THEMES
from themes.widgets import RadioImageFilterSelect


class SimpleContentForm(PictureForm):

    def __init__(self, *args, **kwargs):
        super(SimpleContentForm, self).__init__(*args, **kwargs)
        # TODO: Find out a better way to do this
        page_datalist = SitePage.site_objects.links_from_page('/home')
        self.fields['link_url'].widget = TextInput(
            datalist=tuple(page_datalist))

    class Meta:
        model = SimpleContent
        fields = ('title', 'sub_title', 'short_content',
                  'link_url', 'link_label', 'picture', 'picture_filter',
                  'picture_cropping',)
        widgets = {
            'picture': CustomCropImageWidget(SimpleContent, 'picture'),
            'picture_filter': RadioImageFilterSelect,
        }
