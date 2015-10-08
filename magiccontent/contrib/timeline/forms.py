# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.contrib.auth import get_user_model

import floppyforms.__future__ as forms

from magiccontent.widgets import DatePicker
from .models import TimelineEventContent

User = get_user_model()


class TimelineEventContentForm(forms.ModelForm):

    class Meta:
        model = TimelineEventContent
        fields = ('title', 'created', 'entry_access', 'long_content', 'tags', )
        widgets = {
            'created': DatePicker
        }


class TimelineEventContentCreateForm(forms.ModelForm):

    class Meta:
        model = TimelineEventContent
        fields = ('title',)
