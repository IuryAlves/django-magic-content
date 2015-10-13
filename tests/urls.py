from __future__ import absolute_import

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',  # noqa
    url(r'', include('magiccontent.urls')),
    url(r'^contrib/', include('magiccontent.contrib.textimagecontent.urls')),
    url(r'^contrib/', include('magiccontent.contrib.background.urls')),
    url(r'^contrib/', include('magiccontent.contrib.iconcontent.urls')),
    url(r'^contrib/', include('magiccontent.contrib.imagecontent.urls')),
    url(r'^contrib/', include('magiccontent.contrib.formattedtextimagecontent.urls')),
    url(r'^contrib/', include('magiccontent.contrib.dividertextcontent.urls')),
)


urlpatterns += patterns(
    'django.contrib.auth.views',
    # login page, required by some tests
    url(r'^accounts/login/$', 'login', {'template_name': 'blank.html'}),
    url(r'^auth/login/$', 'login', {'template_name': 'blank.html'}),
)
