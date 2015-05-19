# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms
from floppyforms.widgets import TextInput

# TODO: dependency to NAVIGATION
from navigation.models import SitePage

from .models import IconContent

# TODO: dependency to THEMES
from themes.widgets import RadioIconSelect


class IconContentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IconContentForm, self).__init__(*args, **kwargs)
        # TODO: Find out a better way to do this
        page_datalist = SitePage.site_objects.links_from_page('/home')
        self.fields['link_url'].widget = TextInput(
            datalist=tuple(page_datalist))

    class Meta:
        model = IconContent
        fields = ('title', 'short_content', 'icon', 'link_url', 'link_label',)
        widgets = {
            'icon': RadioIconSelect,
        }
