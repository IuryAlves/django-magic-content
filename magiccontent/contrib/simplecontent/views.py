# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from magiccontent.mixins import (EditableMixin, CreateContentMixin,
                                 ListContentMixin)
from .models import SimpleContent
from .forms import SimpleContentForm


class SimpleContentMixin(object):
    model = SimpleContent
    form_class = SimpleContentForm
    template_name = 'magiccontent/simplecontent_form.html'


class SimpleContentCreateView(CreateContentMixin, SimpleContentMixin,
                              EditableMixin, CreateView):
    pass


class SimplecontentUpdateView(SimpleContentMixin, EditableMixin, UpdateView):
    pass


class SimplecontentDeleteView(SimpleContentMixin, EditableMixin, DeleteView):
    pass


class SimpleContentOrderListView(ListContentMixin, SimpleContentMixin,
                                 ListView):
    pass
