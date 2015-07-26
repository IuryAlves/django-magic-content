# -*- coding: utf-8 -*-
from __future__ import absolute_import

import floppyforms.__future__ as forms

from magiccontent.models import SiteLink
from magiccontent.forms import PictureForm
from magiccontent.widgets import CustomCropImageWidget
from .models import PageLink


class PageLinkForm(PictureForm):

    def __init__(self, *args, **kwargs):
        super(PageLinkForm, self).__init__(*args, **kwargs)
        links_datalist = SiteLink.site_objects.all()

        self.fields['link'] = forms.CharField(
            widget=forms.TextInput(datalist=tuple(links_datalist)),
            required=False)

    class Meta:
        model = PageLink
        fields = ('title', 'sub_title',
                  'link_label', 'picture', 'picture_cropping',)
        widgets = {
            'picture': CustomCropImageWidget(PageLink, 'picture'),
        }

    def save(self, commit=True, *args, **kws):
        instance = super(PageLinkForm, self).save(commit=False, *args, **kws)
        data = self.cleaned_data
        link = data.get('link')

        # try to find the link in SiteLink, if not, creates the link
        if link:
            site_links = SiteLink.site_objects.filter(name=link)

            if site_links:
                # if for some reason there are more than 1 link with same name
                # for same site, it uses the first one found
                site_link = site_links[0]
            else:
                link_name = data.get('link_label', link)
                site_link = SiteLink.site_objects.create(
                    url=link, name=link_name)

            instance.site_link = site_link

        instance.save()
