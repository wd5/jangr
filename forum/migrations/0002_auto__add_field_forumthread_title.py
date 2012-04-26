# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ForumThread.title'
        db.add_column('forum_forumthread', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ForumThread.title'
        db.delete_column('forum_forumthread', 'title')


    models = {
        'forum.forumpost': {
            'Meta': {'object_name': 'ForumPost'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forum.ForumThread']"})
        },
        'forum.forumsection': {
            'Meta': {'object_name': 'ForumSection'},
            'can_have_threads': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forum.ForumSection']", 'null': 'True', 'blank': 'True'})
        },
        'forum.forumthread': {
            'Meta': {'object_name': 'ForumThread'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forum.ForumSection']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['forum']
