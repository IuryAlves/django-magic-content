# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView

from magiccontent.mixins import CreateContentMixin, EditableMixin
from magiccontent.views import MagicDeleteView
from .models import BackgroundArea
from .forms import BackgroundAreaForm


class BackgroundAreaMixin(object):
    model = BackgroundArea
    form_class = BackgroundAreaForm
    template_name = 'magiccontent/background_form.html'


class BackgroundAreaUpdateView(BackgroundAreaMixin, EditableMixin, UpdateView):
    pass


class BackgroundAreaCreateView(CreateContentMixin, BackgroundAreaMixin,
                               EditableMixin, CreateView):
    pass


class BackgroundAreaDeleteView(BackgroundAreaMixin, EditableMixin,
                               MagicDeleteView):
    pass
