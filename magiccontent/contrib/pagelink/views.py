# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from magiccontent.mixins import EditableMixin, CreateContentMixin
from .models import PageLink
from .forms import PageLinkForm


class PageLinkMixin(object):
    model = PageLink
    form_class = PageLinkForm
    template_name = 'magiccontent/simplecontent_form.html'


class PageLinkCreateView(CreateContentMixin, PageLinkMixin, EditableMixin,
                         CreateView):
    pass


class PageLinkUpdateView(PageLinkMixin, EditableMixin, UpdateView):
    pass


class PageLinkDeleteView(PageLinkMixin, EditableMixin, DeleteView):
    pass
