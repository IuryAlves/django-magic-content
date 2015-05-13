# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models as dj_models

import os
import importlib
import inspect


def get_model_for_widget_type(widget_type):
    ''' returns the first BaseContent child of a given contrib app by its
        widget_type '''

    module_name = 'magiccontent.contrib.{0}.models'.format(widget_type)
    module = importlib.import_module(module_name)

    model = None

    for _, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, dj_models):
            if obj._meta.abstract:
                continue
            model = obj

    # SimpleContent by default (old behaviour, should we keep this?)
    if model is None:
        simple_content_module = importlib.import_module(
            'magiccontent.contrib.simplecontent.models')
        model = getattr(simple_content_module, 'SimpleContent')

    return model


def get_contrib_models_module():
    contrib = importlib.import_module('magiccontent.contrib')

    contrib_apps = []
    subapps = filter(lambda i: '.py' not in i, os.listdir(contrib.__path__[0]))

    for subapp_name in subapps:
        import_name = 'magiccontent.contrib.{0}.models'.format(subapp_name)
        contrib_apps.append(importlib.import_module(import_name))

    return contrib_apps


def get_widget_types():
    contrib_models = get_contrib_models_module()

    widget_types = []

    for app_model in contrib_models:
        for _, obj in inspect.getmembers(app_model):
            if inspect.isclass(obj) and issubclass(obj, dj_models):
                if obj._meta.abstract:
                    continue
                widget_types.append((obj._widget_type, obj.__name__))
                break

    return widget_types
