# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView

from magiccontent.mixins import (EditableMixin, CreateContentMixin,
                                 ListContentMixin)
from magiccontent.views import MagicDeleteView
from .models import LongContent
from .forms import LongContentForm, LongContentCreateForm


class LongContentMixin(object):
    model = LongContent
    form_class = LongContentForm
    template_name = 'magiccontent/defaultcontent_form.html'


class LongContentCreateView(CreateContentMixin, LongContentMixin,
                            EditableMixin, CreateView):
    form_class = LongContentCreateForm


class LongContentUpdateView(LongContentMixin, EditableMixin, UpdateView):
    pass


class LongContentDeleteView(LongContentMixin, EditableMixin, MagicDeleteView):
    pass


class LongContentOrderListView(ListContentMixin, LongContentMixin, ListView):
    pass
