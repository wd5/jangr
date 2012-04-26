# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Artist'
        db.create_table('archive_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from=None, db_index=True)),
            ('years_active', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default='\xd0\xa1\xd0\xbe\xd1\x84\xd0\xb8\xd1\x8f', max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('archive', ['Artist'])

        # Adding model 'Song'
        db.create_table('archive_song', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from=None, db_index=True)),
            ('original_artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.Artist'])),
        ))
        db.send_create_signal('archive', ['Song'])

        # Adding model 'SongMedia'
        db.create_table('archive_songmedia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.Song'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from=None, db_index=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='nil', max_length=3)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('archive', ['SongMedia'])


    def backwards(self, orm):
        
        # Deleting model 'Artist'
        db.delete_table('archive_artist')

        # Deleting model 'Song'
        db.delete_table('archive_song')

        # Deleting model 'SongMedia'
        db.delete_table('archive_songmedia')


    models = {
        'archive.artist': {
            'Meta': {'object_name': 'Artist'},
            'city': ('django.db.models.fields.CharField', [], {'default': "'\\xd0\\xa1\\xd0\\xbe\\xd1\\x84\\xd0\\xb8\\xd1\\x8f'", 'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'years_active': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'})
        },
        'archive.song': {
            'Meta': {'object_name': 'Song'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Artist']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'archive.songmedia': {
            'Meta': {'object_name': 'SongMedia'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Song']"}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'nil'", 'max_length': '3'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['archive']
