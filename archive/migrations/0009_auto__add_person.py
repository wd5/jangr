# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Person'
        db.create_table('archive_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('born', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('died', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('archive', ['Person'])


    def backwards(self, orm):
        
        # Deleting model 'Person'
        db.delete_table('archive_person')


    models = {
        'archive.artist': {
            'Meta': {'object_name': 'Artist'},
            'city': ('django.db.models.fields.CharField', [], {'default': "'\\xd0\\xa1\\xd0\\xbe\\xd1\\x84\\xd0\\xb8\\xd1\\x8f'", 'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'picture': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'years_active': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'})
        },
        'archive.person': {
            'Meta': {'object_name': 'Person'},
            'born': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'died': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
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
