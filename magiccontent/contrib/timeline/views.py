# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.sites.models import Site

from accounts.mixins import CanEditMixin

from magiccontent.models import Widget
from magiccontent.mixins import EditableMixin, ListContentMixin
from .models import EntryAuthor, TimelineEventContent
from .forms import TimelineEventContentForm


class TimelineEventContentMixin(object):
    model = TimelineEventContent
    form_class = TimelineEventContentForm
    template_name = 'magiccontent/simplecontent_form.html'

    def form_valid(self, form):
        widget = Widget.site_objects.get(pk=self.kwargs['widget_pk'])
        author, _ = EntryAuthor.objects.get_or_create(user=self.request.user)
        self.object = form.save(commit=False)
        self.object.widget = widget
        self.object.entry_author = author
        # TODO: remove it from here
        self.object.site = Site.objects.get_current()
        self.object.save()
        form.save_m2m()
        return redirect(self.get_success_url())


class TimelineEventContentCreateView(TimelineEventContentMixin,
                                     EditableMixin, CreateView):
    pass


class TimelineEventContentUpdateView(TimelineEventContentMixin,
                                     EditableMixin, UpdateView):
    pass


class TimelineEventContentDeleteView(TimelineEventContentMixin,
                                     EditableMixin, DeleteView):
    pass


class TimelineEventContentOrderListView(ListContentMixin,
                                        TimelineEventContentMixin, ListView):
    pass


class EntryDetailView(DetailView):
    model = TimelineEventContent
    template_name = 'magiccontent/entrycontent/detail.html'

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
