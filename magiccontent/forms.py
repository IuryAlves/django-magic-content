# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
import floppyforms.__future__ as forms

from magiccontent.widgets import (RadioWidgetTypeSelect,
                                  RadioWidgetTypeAllSelect,
                                  RadioWidgetStyleSelect, )

from .models import Area, Widget, SiteLink, WIDGET_TYPES
from .abstract_models import BaseContent


class LinkableFormMixin(object):

    def __init__(self, *args, **kws):
        super(LinkableFormMixin, self).__init__(*args, **kws)
        # by default Django uses the default manager to populate the field
        self.fields['site_link'].queryset = SiteLink.site_objects.all()
        self.fields['custom_link_url'] = forms.URLField(required=False)

    def save(self, *args, **kws):
        data = self.cleaned_data
        custom_link_url = data.pop('custom_link_url')

        if custom_link_url:
            link_name = data.get('link_label') or data.get('title')
            site_link, _ = SiteLink.site_objects.get_or_create(
                name=link_name, defaults={'url': custom_link_url})
            self.cleaned_data['site_link'] = site_link

        super(LinkableFormMixin, self).save(*args, **kws)


class PictureForm(forms.ModelForm):

    ''' A simple form to manage picture fields '''

    remove_picture = forms.BooleanField(required=False)

    def __init__(self, *args, **kws):
        super(PictureForm, self).__init__(*args, **kws)
        instance = kws.get('instance')

        # do not show pictures fields in object creation
        if instance is None:
            del self.fields['remove_picture']
            if self.fields.get('picture_filter'):
                del self.fields['picture_filter']
            del self.fields['picture_cropping']
        else:
            # do not show picture's editing fields if there is no picture
            if not instance.picture:
                del self.fields['remove_picture']
                if self.fields.get('picture_filter'):
                    del self.fields['picture_filter']
                del self.fields['picture_cropping']

        if self.fields.get('picture_filter'):
            filter_list = [(imagefilter, instance.picture)
                           for imagefilter, description
                           in BaseContent.PICTURE_FILTERS]
            self.fields['picture_filter'].choices = filter_list

    def save(self, *args, **kws):
        instance = super(PictureForm, self).save(*args, **kws)
        if self.cleaned_data.get('remove_picture'):
            instance.picture = None
            instance.save()
        return instance


class AreaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AreaForm, self).__init__(*args, **kwargs)
        widget_list = [(widget.id, widget) for widget
                       in Widget.site_objects.list_content_widgets()]
        self.fields['widget'].choices = widget_list

    class Meta:
        model = Area
        fields = ('widget',)
        widgets = {
            'widget': RadioWidgetTypeSelect,
        }


class WidgetForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(WidgetForm, self).__init__(*args, **kwargs)
        widget = kwargs['instance']
        self.fields['style_template'] = forms.ChoiceField(
            label=_('Template Style'),
            choices=widget.widget_types_list(),
            widget=RadioWidgetStyleSelect())

    class Meta:
        model = Widget
        fields = ('description', 'style_template', )


class NewWidgetForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewWidgetForm, self).__init__(*args, **kwargs)
        # TODO: this items shouldn't be fix
        # TODO: the magiccontent shouldn't know about the children
        exclude = ['background', 'pagelink',
                   'menuitem', 'faq', ]
        widget_types = [(id, label)
                        for id, label in WIDGET_TYPES if id not in exclude]
        self.fields['widget_type'].choices = widget_types

    class Meta:
        model = Widget
        fields = ('widget_type', 'name', )
        widgets = {
            'widget_type': RadioWidgetTypeAllSelect,
        }
