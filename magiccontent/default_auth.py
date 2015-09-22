# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

import logging


logger = logging.getLogger('magiccontent.default_auth')


def naive_can_edit(request):
    logger.warning(
        ('naive_can_edit method has been used, please provide a '
         'MAGICCONTENT_CAN_EDIT_METHOD to improve the content security'))
    if request.user.is_authenticated() and request.user.is_staff:
        return True
    return False
