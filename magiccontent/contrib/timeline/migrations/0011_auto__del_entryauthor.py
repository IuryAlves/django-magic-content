# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'EntryAuthor'
        db.delete_table(u'timeline_entryauthor')


    def backwards(self, orm):
        # Adding model 'EntryAuthor'
        db.create_table(u'timeline_entryauthor', (
            ('about', self.gf('django.db.models.fields.TextField')(blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'timeline', ['EntryAuthor'])


    models = {
        u'magiccontent.widget': {
            'Meta': {'object_name': 'Widget'},
            'description': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_content_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u'i8W0y7fs8bBa'", 'max_length': '50'}),
            'style_template': ('django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '128'}),
            'widget_type': ('django.db.models.fields.CharField', [], {'default': "u'simplecontent'", 'max_length': '32'})
        },
        u'magicgallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        },
        u'magicgallery.galleryitem': {
            'Meta': {'object_name': 'GalleryItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magicgallery.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': "u''", 'max_length': '100', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'timeline.timelineeventcontent': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'TimelineEventContent'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'entry_access': ('django.db.models.fields.CharField', [], {'default': "u'public'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link_label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'link_url': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'long_content': ('ckeditor.fields.RichTextField', [], {'default': "u''", 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magicgallery.GalleryItem']", 'null': 'True', 'blank': 'True'}),
            'picture_filter': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            'short_content': ('django.db.models.fields.TextField', [], {'default': "u'Edit content'", 'max_length': '512', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Edit title'", 'max_length': '128', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magiccontent.Widget']"})
        }
    }

    complete_apps = ['timeline']