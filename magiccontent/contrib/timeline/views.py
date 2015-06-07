# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from magiccontent.mixins import (EditableMixin, CreateContentMixin,
                                 ListContentMixin)
from .models import EntryContent
from .forms import EntryContentForm


class EntryContentMixin(object):
    model = EntryContent
    form_class = EntryContentForm
    template_name = 'magiccontent/simplecontent_form.html'


class EntryContentCreateView(CreateContentMixin, EntryContentMixin,
                             EditableMixin, CreateView):
    pass


class EntryContentUpdateView(EntryContentMixin, EditableMixin, UpdateView):
    pass


class EntryContentDeleteView(EntryContentMixin, EditableMixin, DeleteView):
    pass


class EntryContentOrderListView(ListContentMixin, EntryContentMixin, ListView):
    pass
