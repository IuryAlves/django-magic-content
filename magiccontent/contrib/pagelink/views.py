# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView

from magiccontent.mixins import EditableMixin, CreateContentMixin
from magiccontent.views import MagicDeleteView, PictureUpdateView
from .models import PageLink
from .forms import PageLinkForm, PageLinkCreateForm


class PageLinkMixin(object):
    model = PageLink
    form_class = PageLinkForm
    template_name = 'magiccontent/defaultcontent_form.html'


class PageLinkCreateView(CreateContentMixin, PageLinkMixin, EditableMixin,
                         CreateView):
    form_class = PageLinkCreateForm


class PageLinkUpdateView(PageLinkMixin, EditableMixin, UpdateView):
    pass


class PageLinkPictureUpdateView(PageLinkMixin, EditableMixin,
                                PictureUpdateView):
    pass


class PageLinkDeleteView(PageLinkMixin, EditableMixin, MagicDeleteView):
    pass
