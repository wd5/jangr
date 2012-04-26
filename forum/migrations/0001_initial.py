# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ForumSection'
        db.create_table('forum_forumsection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forum.ForumSection'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('can_have_threads', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('forum', ['ForumSection'])

        # Adding model 'ForumThread'
        db.create_table('forum_forumthread', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forum.ForumSection'])),
        ))
        db.send_create_signal('forum', ['ForumThread'])

        # Adding model 'ForumPost'
        db.create_table('forum_forumpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forum.ForumThread'])),
        ))
        db.send_create_signal('forum', ['ForumPost'])


    def backwards(self, orm):
        
        # Deleting model 'ForumSection'
        db.delete_table('forum_forumsection')

        # Deleting model 'ForumThread'
        db.delete_table('forum_forumthread')

        # Deleting model 'ForumPost'
        db.delete_table('forum_forumpost')


    models = {
        'forum.forumpost': {
            'Meta': {'object_name': 'ForumPost'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forum.ForumThread']"})
        },
        'forum.forumsection': {
            'Meta': {'object_name': 'ForumSection'},
            'can_have_threads': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forum.ForumSection']", 'null': 'True', 'blank': 'True'})
        },
        'forum.forumthread': {
            'Meta': {'object_name': 'ForumThread'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forum.ForumSection']"})
        }
    }

    complete_apps = ['forum']
