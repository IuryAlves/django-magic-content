# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models

from magiccontent.abstract_models import BaseContent


class IconContent(BaseContent):

    _widget_type = 'iconcontent'

    FONTAWESOME_ICONS = (
        ('fa-adjust', 'adjust'), ('fa-arrows', 'arrows'),
        ('fa-barcode', 'barcode'), ('fa-bars', 'bars'),
        ('fa-beer', 'beer'), ('fa-bell', 'bell'), ('fa-bolt', 'bolt'),
        ('fa-bomb', 'bomb'), ('fa-book', 'book'), ('fa-bookmark', 'bookmark'),
        ('fa-briefcase', 'briefcase'), ('fa-bug', 'bug'),
        ('fa-building', 'building'), ('fa-bullhorn', 'bullhorn'),
        ('fa-bullseye', 'bullseye'), ('fa-calendar', 'calendar'),
        ('fa-camera', 'camera'), ('fa-car', 'car'),
        ('fa-caret-square-o-down', 'caret-square-o-down'),
        ('fa-caret-square-o-left', 'caret-square-o-left'),
        ('fa-caret-square-o-right', 'caret-square-o-right'),
        ('fa-caret-square-o-up', 'caret-square-o-up'),
        ('fa-certificate', 'certificate'), ('fa-check', 'check'),
        ('fa-child', 'child'), ('fa-circle', 'circle'),
        ('fa-clock-o', 'clock-o'), ('fa-sort-desc', 'sort-desc'),
        ('fa-space-shuttle', 'space-shuttle'), ('fa-spinner', 'spinner'),
        ('fa-spoon', 'spoon'), ('fa-square', 'square'),
        ('fa-star', 'star'), ('fa-star-half', 'star-half'),
        ('fa-suitcase', 'suitcase'), ('fa-sun-o', 'sun-o'),
        ('fa-tablet', 'tablet'), ('fa-tachometer', 'tachometer'),
        ('fa-tag', 'tag'), ('fa-tags', 'tags'),
        ('fa-tasks', 'tasks'), ('fa-taxi', 'taxi'),
        ('fa-terminal', 'terminal'), ('fa-thumb-tack', 'thumb-tack'),
        ('fa-thumbs-down', 'thumbs-down'),
        ('fa-thumbs-o-down', 'thumbs-o-down'),
        ('fa-thumbs-o-up', 'thumbs-o-up'), ('fa-thumbs-up', 'thumbs-up'),
        ('fa-ticket', 'ticket'), ('fa-times', 'times'),
        ('fa-times-circle', 'times-circle'), ('fa-tint', 'tint'),
        ('fa-tree', 'tree'), ('fa-trophy', 'trophy'), ('fa-truck', 'truck'),
        ('fa-umbrella', 'umbrella'), ('fa-university', 'university'),
        ('fa-unlock', 'unlock'), ('fa-upload', 'upload'),
        ('fa-user', 'user'), ('fa-users', 'users'),
        ('fa-video-camera', 'video-camera'), ('fa-volume-down', 'volume-down'),
        ('fa-wheelchair', 'wheelchair'),
    )
    """ title, shorttext and icon """
    icon = models.CharField(_('icon'), max_length=64, default='fa-check',
                            choices=FONTAWESOME_ICONS)

    def _content(self):
        return self.short_content

    @property
    def enable_picture(self):
        return False

    @classmethod
    def style_list(cls):
        style_list = (
            ('default', 'IconContent - Small Icons (default)'),
            ('bigicons', 'IconContent - Big Icons'),
            ('circledicons', 'IconContent - Circled Icons'), )
        return style_list
