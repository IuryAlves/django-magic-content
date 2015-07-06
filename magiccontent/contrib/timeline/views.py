# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.sites.models import Site

from magiccontent.models import Widget
from magiccontent.mixins import EditableMixin, ListContentMixin
from magiccontent.views import MagicDeleteView

from ...mixins import CanEditMixin
from .models import TimelineEventContent
from .forms import TimelineEventContentForm


# TODO: Use the generic Mixin instead
class TimelineEventContentMixin(object):
    model = TimelineEventContent
    form_class = TimelineEventContentForm
    template_name = 'magiccontent/simplecontent_form.html'

    def form_valid(self, form):
        widget = Widget.site_objects.get(pk=self.kwargs['widget_pk'])
        self.object = form.save(commit=False)
        self.object.widget = widget
        self.object.site = Site.objects.get_current()
        self.object.save()
        return redirect(self.get_success_url())


class TimelineEventContentCreateView(TimelineEventContentMixin,
                                     EditableMixin, CreateView):
    pass


class TimelineEventContentUpdateView(TimelineEventContentMixin,
                                     EditableMixin, UpdateView):
    pass


class TimelineEventContentDeleteView(TimelineEventContentMixin,
                                     EditableMixin, MagicDeleteView):
    pass


class TimelineEventContentOrderListView(ListContentMixin,
                                        TimelineEventContentMixin, ListView):
    pass


class EntryDetailView(DetailView):
    model = TimelineEventContent
    template_name = 'magiccontent/timelineeventcontent/detail.html'

    def get_context_data(self, **kwargs):
        context = super(EntryDetailView,
                        self).get_context_data(**kwargs)
        entry = get_object_or_404(TimelineEventContent,
                                  pk=self.kwargs.get('pk', None))
        context['widget'] = entry.widget
        return context


class ShowTimelineEventContentPageView(CanEditMixin, TemplateView):
    template_name = "magiccontent/timeline.html"

    def get_context_data(self, **kwargs):
        context = super(ShowTimelineEventContentPageView,
                        self).get_context_data(**kwargs)
        widget = get_object_or_404(Widget, pk=self.kwargs.get('pk', None))
        context['widget'] = widget
        context['content_list'] = widget.get_widget_type.objects.filter(
            widget=widget)
        return context
