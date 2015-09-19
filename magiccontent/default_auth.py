# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import


def naive_can_edit(request):
    if request.user.is_authenticated() and request.user.is_staff:
        return True
    return False
