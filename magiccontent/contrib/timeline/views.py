# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404

from magiccontent.models import Widget
from magiccontent.mixins import (CreateContentMixin, EditableMixin,
                                 ListContentMixin, )
from magiccontent.views import MagicDeleteView, PictureUpdateView

from ...mixins import CanEditMixin
from .models import TimelineEventContent
from .forms import TimelineEventContentForm, TimelineEventContentCreateForm


# TODO: Use the generic Mixin instead
class TimelineEventContentMixin(object):
    model = TimelineEventContent
    form_class = TimelineEventContentForm
    template_name = 'magiccontent/defaultcontent_form.html'


class TimelineEventContentCreateView(CreateContentMixin, TimelineEventContentMixin,
                                     EditableMixin, CreateView):
    form_class = TimelineEventContentCreateForm


class TimelineEventContentUpdateView(TimelineEventContentMixin,
                                     EditableMixin, UpdateView):
    pass


class TimelineEventContentPictureUpdateView(TimelineEventContentMixin, EditableMixin,
                                            PictureUpdateView):
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
