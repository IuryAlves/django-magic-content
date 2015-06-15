# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.contrib.auth import get_user_model

import floppyforms.__future__ as forms

from .models import EntryContent

User = get_user_model()


class EntryContentForm(forms.ModelForm):

    class Meta:
        model = EntryContent
        fields = ('title', 'entry_access', 'long_content', 'tags', )
