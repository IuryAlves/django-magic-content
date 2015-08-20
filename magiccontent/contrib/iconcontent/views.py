# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView

from magiccontent.mixins import (EditableMixin, CreateContentMixin,
                                 ListContentMixin)
from magiccontent.views import MagicDeleteView
from .models import IconContent
from .forms import IconContentForm


class IconContentMixin(object):
    model = IconContent
    form_class = IconContentForm
    template_name = 'magiccontent/defaultcontent_form.html'


class IconContentCreateView(CreateContentMixin, IconContentMixin,
                            EditableMixin, CreateView):
    pass


class IconContentUpdateView(IconContentMixin, EditableMixin, UpdateView):
    pass


class IconContentDeleteView(IconContentMixin, EditableMixin, MagicDeleteView):
    pass


class IconContentOrderListView(ListContentMixin, IconContentMixin, ListView):
    pass
