# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django import test
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model

from magicthemes.models import ThemePreferences


User = get_user_model()


class AuthTestCase(test.TestCase):

    def setUp(self):
        self.user_credentials = {
            'username': 'admin', 'email': 'admin@admin.com', 'password': '123'}
        create_params = self.user_credentials.copy()
        password = create_params.pop('password')

        self.site = Site.objects.create(domain='example.com')
        ThemePreferences.objects.create(site=self.site)

        self.user = User.objects.create(
            is_staff=True, is_superuser=True, **create_params)
        self.user.set_password(password)
        self.user.save()

    def login_user(self):
        logged_in = self.client.login(
            username=self.user_credentials['username'],
            password=self.user_credentials['password'])
        self.assertTrue(logged_in)

    def logout_user(self):
        self.client.logout()
