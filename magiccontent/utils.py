# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

import importlib

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_can_edit_method(settings_name):
    """
        Returns the user's defined method for who can edit contents
    """
    permission_settings = getattr(settings, settings_name, None)

    if not permission_settings:
        raise ImproperlyConfigured(
            'The settings.{0} param is not defined.'.format(settings_name))
    module_name, method_name = permission_settings.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, method_name)
