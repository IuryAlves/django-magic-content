# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Area.is_landingpage_area'
        db.add_column(u'magiccontent_area', 'is_landingpage_area',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Area.is_landingpage_area'
        db.delete_column(u'magiccontent_area', 'is_landingpage_area')


    models = {
        u'magiccontent.area': {
            'Meta': {'ordering': "[u'id']", 'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_always_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_landingpage_area': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magiccontent.Widget']", 'null': 'True'})
        },
        u'magiccontent.sitelink': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'SiteLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'origin_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'origin_model_pk': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'default': "u'landingpage'", 'max_length': '20', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'magiccontent.widget': {
            'Meta': {'object_name': 'Widget'},
            'description': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_content_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u'KlwSWxQevDHD'", 'max_length': '50'}),
            'style_template': ('django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '128'}),
            'widget_type': ('django.db.models.fields.CharField', [], {'default': "u'simplecontent'", 'max_length': '32'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['magiccontent']