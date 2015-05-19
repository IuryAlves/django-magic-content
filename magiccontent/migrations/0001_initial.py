# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Area'
        db.create_table(u'magiccontent_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('widget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magiccontent.Widget'], null=True)),
            ('is_visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_always_visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'magiccontent', ['Area'])

        # Adding model 'Widget'
        db.create_table(u'magiccontent_widget', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(default=u'xuWKLotVwMqC', max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64, db_index=True)),
            ('widget_type', self.gf('django.db.models.fields.CharField')(default=u'simplecontent', max_length=32)),
            ('style_template', self.gf('django.db.models.fields.CharField')(default=u'default', max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128, blank=True)),
            ('is_content_data', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'magiccontent', ['Widget'])


    def backwards(self, orm):
        # Deleting model 'Area'
        db.delete_table(u'magiccontent_area')

        # Deleting model 'Widget'
        db.delete_table(u'magiccontent_widget')


    models = {
        u'magiccontent.area': {
            'Meta': {'ordering': "[u'id']", 'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_always_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magiccontent.Widget']", 'null': 'True'})
        },
        u'magiccontent.widget': {
            'Meta': {'object_name': 'Widget'},
            'description': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_content_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u'0R99u3TtiYpA'", 'max_length': '50'}),
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