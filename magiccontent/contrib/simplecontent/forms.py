# -*- coding: utf-8 -*-
from __future__ import absolute_import

from magiccontent.forms import PictureForm
from magiccontent.widgets import CustomCropImageWidget, RadioImageFilterSelect
from magiccontent.models import SiteLink

from .models import SimpleContent


class SimpleContentForm(PictureForm):

    def __init__(self, *args, **kws):
        super(SimpleContentForm, self).__init__(*args, **kws)
        # by default Django uses the default manager to populate the field
        self.fields['site_link'].queryset = SiteLink.site_objects.all()

    class Meta:
        model = SimpleContent
        fields = ('title', 'sub_title', 'short_content',
                  'site_link', 'link_label',
                  'picture', 'picture_cropping', 'picture_filter',)
        widgets = {
            'picture': CustomCropImageWidget(SimpleContent, 'picture'),
            'picture_filter': RadioImageFilterSelect,
        }
