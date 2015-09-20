# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models
from multisitesutils.models import Preferences


class SitePreferences(Preferences):
    """ See behaviours.Preferences how to use it """
    title = models.CharField(
        'Site Title', max_length=64, default='title', blank=True)
    name = models.CharField(
        'Site Name', max_length=64, default='name', blank=True)
    footer_title = models.CharField(
        'Footer Title', max_length=128, default='footer title', blank=True)
    footer_address = models.TextField(
        'Address', max_length=256, default='address', blank=True)
    footer_extra = models.TextField(
        'Extra Information', max_length=128, default='extra', blank=True)
