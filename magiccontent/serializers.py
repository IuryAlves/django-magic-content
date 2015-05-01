# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.core.exceptions import ImproperlyConfigured

from rest_framework import serializers

from .models import Area


class AreaVisibleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Area
        fields = ('id', 'is_visible',)


def ContentFieldUpdateSerializer(model_class, content_instance, request_data, _fields=[]):
    """ Generate dynamically a '_fields' serializer for update calls """

    class INContentFieldUpdateSerializer(serializers.
                                         HyperlinkedModelSerializer):

        class Meta:
            model = model_class
            fields = _fields

        def __init__(self, *args, **kwargs):
            if len(_fields) == 0:
                raise ImproperlyConfigured("----> ERROR: It's necessary at least 1 _fields.")
            super(INContentFieldUpdateSerializer, self).__init__(*args, **kwargs)

    return INContentFieldUpdateSerializer(content_instance, request_data)