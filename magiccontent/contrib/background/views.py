# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import UpdateView

from magiccontent.mixins import EditableMixin
from .models import BackgroundArea
from .forms import BackgroundAreaForm


class BackgroundAreaMixin(object):
    model = BackgroundArea
    form_class = BackgroundAreaForm
    template_name = 'magiccontent/simplecontent_form.html'


class BackgroundAreaUpdateView(BackgroundAreaMixin, EditableMixin, UpdateView):
    pass
