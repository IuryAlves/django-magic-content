# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView

from magiccontent.mixins import (EditableMixin, CreateContentMixin,
                                 ListContentMixin)
from magiccontent.views import MagicDeleteView
from .models import SimpleContent
from .forms import SimpleContentForm


class SimpleContentMixin(object):
    model = SimpleContent
    form_class = SimpleContentForm
    template_name = 'magiccontent/simplecontent_form.html'


class SimpleContentCreateView(CreateContentMixin, SimpleContentMixin,
                              EditableMixin, CreateView):
    pass


class SimpleContentUpdateView(SimpleContentMixin, EditableMixin, UpdateView):
    pass


class SimpleContentDeleteView(SimpleContentMixin, EditableMixin,
                              MagicDeleteView):
    pass


class SimpleContentOrderListView(ListContentMixin, SimpleContentMixin,
                                 ListView):
    pass
