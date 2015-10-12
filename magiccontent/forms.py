# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
import floppyforms.__future__ as forms

from magiccontent.widgets import (RadioWidgetTypeSelect,
                                  RadioWidgetTypeAllSelect,
                                  RadioWidgetStyleSelect, )

from .models import Area, Widget, SiteLink, WIDGET_TYPES
from .abstract_models import BaseContent

NEWCUTOMPAGE = 'NEWCUTOMPAGE'


class LinkRefererChoiceField(forms.ModelChoiceField):

    def __init__(self, *args, **kws):
        super(LinkRefererChoiceField, self).__init__(*args, **kws)
        queryset = kws['queryset']

        landingpage = ['Landing Page Links', []]
        for landing in queryset.filter(referer='landingpage'):
            data = (landing.id, landing.name)
            landingpage[1].append(data)

        internalpage = ['Internal Page Links', []]
        for internal in queryset.filter(referer='internalpage'):
            data = (internal.id, internal.name)
            internalpage[1].append(data)

        externalpage = ['External Page Links', []]
        for external in queryset.filter(referer='externalpage'):
            data = (external.id, external.name)
            externalpage[1].append(data)

        self.choices = [('', '---------'), landingpage, internalpage,
                        externalpage]


class LinkableFormMixin(object):

    def __init__(self, *args, **kws):
        super(LinkableFormMixin, self).__init__(*args, **kws)
        # by default Django uses the default manager to populate the field
        newcustompage, _ = SiteLink.site_objects.get_or_create(
            name='>>> Create and link to a new custom page',
            url=NEWCUTOMPAGE)
        self.fields['site_link'] = LinkRefererChoiceField(
            queryset=SiteLink.site_objects.all(), required=False)
        self.fields['link_label'].help_text =\
            ('You can provide a custom name to this link, if not, '
             'the title will be used instead')
        self.fields['custom_link_url'] = forms.URLField(
            required=False, help_text='example: http://www.google.com')

        # for template display purposes
        self.show_link_tools = True

    def clean(self):
        data = self.cleaned_data

        link = data.get('site_link')
        label = data.get('link_label') or data.get('title')
        if link:

            if link.url == NEWCUTOMPAGE and label:
                site_link, created = SiteLink.site_objects.get_or_create(
                    name='Page: {0}'.format(label),
                    url='/page/{0}/'.format(slugify(label).replace('-', '')),
                    defaults={'referer': 'internalpage'})
                data['site_link'] = site_link

        custom_link_url = data.pop('custom_link_url', '')
        if custom_link_url:
            _link_name = label or data.get('title')
            link_name = '{0} - {1}'.format(
                _link_name, custom_link_url)[:64]
            site_link, sl_created = SiteLink.site_objects.get_or_create(
                name=link_name,
                defaults={'url': custom_link_url, 'referer': 'externalpage'})
            self.cleaned_data['link_label'] = _link_name
            self.cleaned_data['site_link'] = site_link

        return data


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
        exclude = ['background', 'dividertextcontent',
                   'menuitem', 'faq', ]
        widget_types = [(id, label)
                        for id, label in WIDGET_TYPES if id not in exclude]
        self.fields['widget_type'].choices = widget_types

    class Meta:
        model = Widget
        fields = ('name', 'widget_type', )
        widgets = {
            'widget_type': RadioWidgetTypeAllSelect,
        }
        help_texts = {
            'name': "e.g: News, Sports, What's on ...",
        }