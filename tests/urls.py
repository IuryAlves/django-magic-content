from __future__ import absolute_import

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',  # noqa
    url(r'', include('magiccontent.urls')),
)


urlpatterns += patterns(
    'django.contrib.auth.views',
    # login page, required by some tests
    url(r'^accounts/login/$', 'login', {'template_name': 'blank.html'}),
    url(r'^auth/login/$', 'login', {'template_name': 'blank.html'}),
)
