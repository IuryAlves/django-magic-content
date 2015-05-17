# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

import importlib
import inspect

from django.conf import settings
from django.views.generic import CreateView, UpdateView, DeleteView

from .abstract_models import BaseContent
from .mixins import ListContentMixin


def get_content_models():
    ''' Returns a list with BaseContent's models
        each row has a dict like:
            {'model_class' : ModelClass, 'model_name': 'modelname'}

        How it works:
        - iterates over all project's applications
        - reads all models.py from these applications
        - retrieves any model that extends magiccontent.models.BaseContent

        Issues:
        - If the model is defined somewhere else instead models.py it will not
          be captured (eg: app/abstract_models.py)
        - This helper has a moderate overhead, try to not use it in request ->
          response process, intead use it on the project's preloader such as
          url definition.
    '''

    apps = map(lambda i: '{0}.models'.format(i), settings.INSTALLED_APPS)
    models_list = []

    for app in apps:
        try:
            app_models = importlib.import_module(app)
        except ImportError:
            continue

        for _, obj in inspect.getmembers(app_models):
            if inspect.isclass(obj) and issubclass(obj, BaseContent):
                if obj._meta.abstract:
                    continue
                data = {'model_class': obj, 'model_name': obj._meta.model_name}
                models_list.append(data)

    return models_list


ALLOWED_VIEWS = [
    {'class': CreateView, 'url_label': 'create'},
    {'class': UpdateView, 'url_label': 'update'},
    {'class': DeleteView, 'url_label': 'delete'},
    {'class': ListContentMixin, 'url_label': 'order'},
]


def content_url_generator(content_model):
    '''  each row has a dict like:
        {'view_class' : ContentView,
         'view_type': 'create, update, delete or order (list)',
         'model_name': 'simplecontent, longcontent...'}

        This helper is for CRUD only, if the view is not a subclass of above
        types it will be skipped.
    '''

    # ListContentMixin is a special case to show order's view
    apps = map(lambda i: '{0}.views'.format(i), settings.INSTALLED_APPS)
    views_list = []

    for app in apps:
        try:
            app_views = importlib.import_module(app)
        except ImportError:
            continue

        for _, obj in inspect.getmembers(app_views):

            for allowed_view in ALLOWED_VIEWS:
                allowed_class = allowed_view['class']
                if inspect.isclass(obj) and issubclass(obj, allowed_class):

                    model = getattr(obj, 'model', None)
                    if not model:
                        continue
                    if model != content_model:
                        continue

                    if issubclass(model, BaseContent):
                        data = {'view_class': obj,
                                'view_type': allowed_view['url_label'],
                                'model_name': model._meta.model_name}
                        views_list.append(data)

                        break

    return views_list


CONTENT_MODELS = get_content_models()
CONTENT_MODEL_NAMES = [i['model_name'] for i in CONTENT_MODELS]
