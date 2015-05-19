# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import importlib
import inspect

# from .abstract_models import BaseContent


def get_model_for_widget_type(widget_type):
    ''' returns the first BaseContent child of a given contrib app by its
        widget_type '''

    # avoid recursivity
    from magiccontent.models import BaseContent

    module_name = 'magiccontent.contrib.{0}.models'.format(widget_type)
    module = importlib.import_module(module_name)

    model = None

    for _, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, BaseContent):
            if obj._meta.abstract:
                continue
            model = obj

    # SimpleContent by default (old behaviour, should we keep this?)
    if model is None:
        simple_content_module = importlib.import_module(
            'magiccontent.contrib.simplecontent.models')
        model = getattr(simple_content_module, 'SimpleContent')

    return model
