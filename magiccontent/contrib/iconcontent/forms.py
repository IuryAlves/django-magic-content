# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms

from magiccontent.widgets import RadioIconSelect
from magiccontent.models import SiteLink

from .models import IconContent


class IconContentForm(forms.ModelForm):

    def __init__(self, *args, **kws):
        super(IconContentForm, self).__init__(*args, **kws)
        # by default Django uses the default manager to populate the field
        self.fields['site_link'].queryset = SiteLink.site_objects.all()

    class Meta:
        model = IconContent
        fields = ('title', 'short_content', 'icon', 'site_link', 'link_label',)
        widgets = {
            'icon': RadioIconSelect,
        }
