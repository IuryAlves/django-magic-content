# -*- coding: utf-8 -*-
from __future__ import absolute_import

from magiccontent.forms import PictureForm
from magiccontent.widgets import CustomCropImageWidget, RadioImageFilterSelect

from magiccontent.models import SiteLink
from .models import LongContent


class LongContentForm(PictureForm):

    def __init__(self, *args, **kws):
        super(LongContentForm, self).__init__(*args, **kws)
        # by default Django uses the default manager to populate the field
        self.fields['site_link'].queryset = SiteLink.site_objects.all()

    class Meta:
        model = LongContent
        fields = ('title', 'long_content', 'site_link', 'link_label',
                  'picture', 'picture_cropping', 'picture_filter', )
        widgets = {
            'picture': CustomCropImageWidget(LongContent, 'picture'),
            'picture_filter': RadioImageFilterSelect,
        }
