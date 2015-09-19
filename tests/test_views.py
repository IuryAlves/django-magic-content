# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from .factories import AreaFactory
from .helpers import AuthTestCase


class AreaUpdateViewTest(AuthTestCase):

    def setUp(self):
        super(AreaUpdateViewTest, self).setUp()

        self.area = AreaFactory(site=self.site)
        self.url = reverse('magiccontent.area.update', args=[self.area.pk])
        self.no_perm_url = '/accounts/login/?next={0}'.format(self.url)

    def test_get_response_with_permission(self):
        self.login_user()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magiccontent/form.html')

    def test_get_response_without_permission(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.no_perm_url)

    def test_post_response_with_permission(self):
        pass

    def test_post_response_without_permission(self):
        pass

    def test_post_with_valid_widget(self):
        pass

    def test_post_with_invalid_widget(self):
        pass
