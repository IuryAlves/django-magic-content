# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.core.management.base import BaseCommand

from magiccontent.models import SiteLink
from magiccontent.link_utils import SITE_LINKS


class Command(BaseCommand):
    ''' Generates all links to the current site '''

    def handle(self, *args, **options):
        SiteLink.site_objects.all().delete()

        for link in SITE_LINKS:
            SiteLink.site_objects.create(name=link['name'], url=link['url'])

        print('{0} links generated'.format(len(SITE_LINKS)))
