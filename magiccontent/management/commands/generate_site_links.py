# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from optparse import make_option

from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site

from magiccontent.models import SiteLink
from magiccontent.link_utils import SITE_LINKS


class Command(BaseCommand):
    ''' Generates all links to the current site
        Note: call this command only on setup.

        BEWARE: This command is destructive, use it ONLY ON SITE SETUP.
                Any custom links added by users for the given site will be
                destroyed.
    '''

    option_list = BaseCommand.option_list + (
        make_option('--site-id', action='store', dest='site_id',
                    type='int',
                    help='The site ID. Default is the current one'),
    )

    def handle(self, *args, **options):
        site_id = options['site_id']
        if site_id:
            try:
                site = Site.objects.get(id=site_id)
            except Site.DoesNotExist:
                raise Exception('site ID not found')
        else:
            site = Site.objects.get_current()

        SiteLink.objects.filter(site=site).delete()

        for link in SITE_LINKS:
            SiteLink.objects.create(
                site=site, name=link['name'], url=link['url'])

        print('{0} links generated'.format(len(SITE_LINKS)))
