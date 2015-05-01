import floppyforms.__future__ as forms


from core.helpers import LinkListForm
from floppyforms.widgets import TextInput

from navigation.models import SitePage

from .models import (Area, Widget, SimpleContent,
                     LongContent, IconContent, PageLink,
                     BackgroundArea, ImageContent, GalleryContent)
from .widgets import CustomCropImageWidget
from themes.widgets import RadioIconSelect, RadioImageFilterSelect


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


class LongContentForm(PictureForm):

    def __init__(self, *args, **kwargs):
        super(LongContentForm, self).__init__(*args, **kwargs)
        # TODO: Find out a better way to do this
        page_datalist = SitePage.site_objects.links_from_page('/home')
        self.fields['link_url'].widget = TextInput(
            datalist=tuple(page_datalist))

    class Meta:
        model = LongContent
        fields = ('title', 'long_content', 'picture', 'picture_cropping',
                  'picture_filter', 'link_url', 'link_label',)
        widgets = {
            'picture': CustomCropImageWidget(LongContent, 'picture'),
            'picture_filter': RadioImageFilterSelect,
        }


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


class ImageContentForm(PictureForm):

    def __init__(self, *args, **kwargs):
        super(ImageContentForm, self).__init__(*args, **kwargs)
        # TODO: Find out a better way to do this
        page_datalist = SitePage.site_objects.links_from_page('/home')
        self.fields['link_url'].widget = TextInput(
            datalist=tuple(page_datalist))

    class Meta:
        model = ImageContent
        fields = ('title', 'short_content', 'picture', 'picture_cropping',
                  'picture_filter', 'link_url',)
        widgets = {
            'picture': CustomCropImageWidget(LongContent, 'picture'),
            'picture_filter': RadioImageFilterSelect,
        }


class BackgroundAreaForm(PictureForm):

    def __init__(self, *args, **kwargs):
        super(BackgroundAreaForm, self).__init__(*args, **kwargs)
        # TODO: Find out a better way to do this
        page_datalist = SitePage.site_objects.links_from_page('/home')
        self.fields['link1_url'].widget = TextInput(
            datalist=tuple(page_datalist))

    class Meta:
        model = BackgroundArea
        fields = (
            'title', 'sub_title', 'short_content', 'link1_url', 'link1_label',
            'picture', 'picture_cropping',)
        widgets = {
            'picture': CustomCropImageWidget(BackgroundArea, 'picture'),
        }


class PageLinkForm(LinkListForm, PictureForm):

    show_links_on_field = 'link1_url'

    class Meta:
        model = PageLink
        fields = ('title', 'sub_title', 'link1_url',
                  'link1_label', 'picture', 'picture_cropping',)
        widgets = {
            'picture': CustomCropImageWidget(PageLink, 'picture'),
        }


class GalleryContentForm(forms.ModelForm):

    class Meta:
        model = GalleryContent
        fields = ('title', 'short_content', 'picture', 'picture_cropping',
                  'picture_filter',)
        widgets = {
            'picture': CustomCropImageWidget(GalleryContent, 'picture'),
            'picture_filter': RadioImageFilterSelect,
        }
