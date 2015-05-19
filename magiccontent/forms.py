# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import floppyforms.__future__ as forms

from .models import Area, Widget


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

    def save(self, *args, **kws):
        instance = super(PictureForm, self).save(*args, **kws)
        if self.cleaned_data.get('remove_picture'):
            instance.picture = None
            instance.save()
        return instance


class AreaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AreaForm, self).__init__(*args, **kwargs)
        widget_list = Widget.site_objects.list_content_widgets()
        self.fields['widget'] = forms.ModelChoiceField(queryset=widget_list)

    class Meta:
        model = Area
        fields = ('widget',)


class WidgetForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(WidgetForm, self).__init__(*args, **kwargs)
        widget = kwargs['instance']
        choices = widget.widget_types_list()
        self.fields['style_template'] = forms.ChoiceField(choices=choices)

    class Meta:
        model = Widget
        fields = ('style_template', 'description',)


class NewWidgetForm(forms.ModelForm):

    class Meta:
        model = Widget
        fields = ('name', 'widget_type',)
