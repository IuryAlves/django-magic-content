# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import EntryAuthor, EntryContent


admin.site.register(EntryAuthor)
admin.site.register(EntryContent)
