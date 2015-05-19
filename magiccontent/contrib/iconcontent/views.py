# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from magiccontent.mixins import (EditableMixin, CreateContentMixin,
                                 ListContentMixin)
from .models import IconContent
from .forms import IconContentForm


class IconContentMixin(object):
    model = IconContent
    form_class = IconContentForm
    template_name = 'magiccontent/simplecontent_form.html'


class IconContentCreateView(CreateContentMixin, IconContentMixin,
                            EditableMixin, CreateView):
    pass


class IconContentUpdateView(IconContentMixin, EditableMixin, UpdateView):
    pass


class IconContentDeleteView(IconContentMixin, EditableMixin, DeleteView):
    pass


class IconContentOrderListView(ListContentMixin, IconContentMixin, ListView):
    pass
