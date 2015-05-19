# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from magiccontent.mixins import (EditableMixin, CreateContentMixin,
                                 ListContentMixin)
from .models import LongContent
from .forms import LongContentForm


class LongContentMixin(object):
    model = LongContent
    form_class = LongContentForm
    template_name = 'magiccontent/simplecontent_form.html'


class LongContentCreateView(CreateContentMixin, LongContentMixin,
                            EditableMixin, CreateView):
    pass


class LongContentUpdateView(LongContentMixin, EditableMixin, UpdateView):
    pass


class LongContentDeleteView(LongContentMixin, EditableMixin, DeleteView):
    pass


class LongContentOrderListView(ListContentMixin, LongContentMixin, ListView):
    pass
