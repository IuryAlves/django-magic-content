# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

import importlib

from django.conf import settings

from .default_auth import naive_can_edit


def get_can_edit_method(settings_name):
    """
        Returns the user's defined method for who can edit contents
    """
    permission_settings = getattr(settings, settings_name, None)

    if permission_settings:

        module_name, method_name = permission_settings.rsplit('.', 1)
        module = importlib.import_module(module_name)
        return getattr(module, method_name)

    return naive_can_edit
