# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TimelineEventContent'
        db.create_table(u'timeline_timelineeventcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('widget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magiccontent.Widget'])),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Edit title', max_length=128, blank=True)),
            ('short_content', self.gf('django.db.models.fields.TextField')(default=u'Edit content', max_length=512, blank=True)),
            ('long_content', self.gf('ckeditor.fields.RichTextField')(default=u'', blank=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magicgallery.GalleryItem'], null=True, blank=True)),
            ('picture_filter', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=99)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('link_url', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('link_label', self.gf('django.db.models.fields.CharField')(default=u'', max_length=64, blank=True)),
            ('entry_author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeline.EntryAuthor'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('entry_access', self.gf('django.db.models.fields.CharField')(default=u'public', max_length=30)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'timeline', ['TimelineEventContent'])


    def backwards(self, orm):
        # Deleting model 'TimelineEventContent'
        db.delete_table(u'timeline_timelineeventcontent')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'magiccontent.widget': {
            'Meta': {'object_name': 'Widget'},
            'description': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_content_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u'MjvGtEoKxKfc'", 'max_length': '50'}),
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
        u'timeline.entryauthor': {
            'Meta': {'object_name': 'EntryAuthor'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'timeline.timelineeventcontent': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'TimelineEventContent'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'entry_access': ('django.db.models.fields.CharField', [], {'default': "u'public'", 'max_length': '30'}),
            'entry_author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.EntryAuthor']", 'null': 'True', 'blank': 'True'}),
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