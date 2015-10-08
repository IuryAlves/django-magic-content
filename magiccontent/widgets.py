# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib.admin.sites import site

from image_cropping.widgets import CropForeignKeyWidget
from floppyforms.widgets import RadioSelect, CheckboxInput, DateInput


class CustomCropImageWidget(CropForeignKeyWidget):
    """ Image Crop Widget for ForeignKey fields
        TODO: find out a way to auto discover the model and field_name params
    """
    def __init__(self, model, field_name):
        super(CustomCropImageWidget, self).__init__(
            model._meta.get_field(field_name).rel, site, field_name=field_name)


class RadioImageFilterSelect(RadioSelect):
    template_name = 'floppyforms/radioimagefilter.html'


class RadioIconSelect(RadioSelect):
    template_name = 'floppyforms/radioicon.html'


class RadioWidgetTypeSelect(RadioSelect):
    template_name = 'floppyforms/radiowidgettype.html'


class RadioWidgetTypeAllSelect(RadioSelect):
    template_name = 'floppyforms/radiowidgettypeall.html'


class RadioWidgetStyleSelect(RadioSelect):
    template_name = 'floppyforms/radiowidgetstyle.html'


class OnOffCheckboxInput(CheckboxInput):
    template_name = 'floppyforms/onoff_checkbox.html'


class YesNoCheckboxInput(CheckboxInput):
    template_name = 'floppyforms/yesno_checkbox.html'


class DatePicker(DateInput):
    template_name = 'floppyforms/datepicker.html'

    class Media:
        js = (
            'frontend/jquery-ui-1.11.4/jquery-ui.min.js',
        )
        css = {
            'all': (
                'frontend/jquery-ui-1.11.4/jquery-ui.min.css',
            )
        }
