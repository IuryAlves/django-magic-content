# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from accounts.mixins import CanEditMixin

from magiccontent.models import Widget
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


class EntryDetailView(DetailView):
    model = EntryContent
    template_name = 'magiccontent/entrycontent/detail.html'

    def get_queryset(self):
        return self.model.objects.filter(
            entry_type=self.kwargs.get('entry_type'))


class ShowEntryContentPageView(CanEditMixin, TemplateView):
    template_name = "magiccontent/timeline.html"

    def get_context_data(self, **kwargs):
        context = super(ShowEntryContentPageView,
                        self).get_context_data(**kwargs)
        widget = get_object_or_404(Widget, pk=self.kwargs.get('pk', None))
        context['widget'] = widget
        context['content_list'] = widget.get_widget_type.objects.filter(
            widget=widget)
        raise Exception(context)
        return context
