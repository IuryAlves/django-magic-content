# -*- coding: utf-8 -*-
from __future__ import absolute_import

from magiccontent.forms import PictureForm
from magiccontent.widgets import CustomCropImageWidget, RadioImageFilterSelect

from magiccontent.models import SiteLink
from .models import ImageContent


class ImageContentForm(PictureForm):

    def __init__(self, *args, **kws):
        super(ImageContentForm, self).__init__(*args, **kws)
        # by default Django uses the default manager to populate the field
        self.fields['site_link'].queryset = SiteLink.site_objects.all()

    class Meta:
        model = ImageContent
        fields = ('title', 'short_content', 'picture', 'picture_cropping',
                  'picture_filter', 'site_link')
        widgets = {
            'picture': CustomCropImageWidget(ImageContent, 'picture'),
            'picture_filter': RadioImageFilterSelect,
        }
