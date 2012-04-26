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
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from=None, db_index=True)),
            ('alive', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('born', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('died', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('archive', ['Person'])

        # Adding model 'Artist'
        db.create_table('archive_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from=None, db_index=True)),
            ('years_active', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default='\xd0\xa1\xd0\xbe\xd1\x84\xd0\xb8\xd1\x8f', max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('archive', ['Artist'])

        # Adding model 'Membership'
        db.create_table('archive_membership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.Person'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.Artist'])),
            ('instrument', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('years', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('now', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('archive', ['Membership'])

        # Adding model 'Song'
        db.create_table('archive_song', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from=None, db_index=True)),
            ('original_artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.Artist'])),
        ))
        db.send_create_signal('archive', ['Song'])

        # Adding model 'Album'
        db.create_table('archive_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from=None, db_index=True)),
            ('released', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal('archive', ['Album'])

        # Adding M2M table for field artists on 'Album'
        db.create_table('archive_album_artists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('album', models.ForeignKey(orm['archive.album'], null=False)),
            ('artist', models.ForeignKey(orm['archive.artist'], null=False))
        ))
        db.create_unique('archive_album_artists', ['album_id', 'artist_id'])

        # Adding model 'AlbumTrack'
        db.create_table('archive_albumtrack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.Song'])),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.Album'])),
            ('number', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('side', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('archive', ['AlbumTrack'])


    def backwards(self, orm):
        
        # Deleting model 'Person'
        db.delete_table('archive_person')

        # Deleting model 'Artist'
        db.delete_table('archive_artist')

        # Deleting model 'Membership'
        db.delete_table('archive_membership')

        # Deleting model 'Song'
        db.delete_table('archive_song')

        # Deleting model 'Album'
        db.delete_table('archive_album')

        # Removing M2M table for field artists on 'Album'
        db.delete_table('archive_album_artists')

        # Deleting model 'AlbumTrack'
        db.delete_table('archive_albumtrack')


    models = {
        'archive.album': {
            'Meta': {'object_name': 'Album'},
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['archive.Artist']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'released': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tracks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['archive.Song']", 'symmetrical': 'False', 'through': "orm['archive.AlbumTrack']", 'blank': 'True'})
        },
        'archive.albumtrack': {
            'Meta': {'object_name': 'AlbumTrack'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Song']"})
        },
        'archive.artist': {
            'Meta': {'object_name': 'Artist'},
            'city': ('django.db.models.fields.CharField', [], {'default': "'\\xd0\\xa1\\xd0\\xbe\\xd1\\x84\\xd0\\xb8\\xd1\\x8f'", 'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['archive.Person']", 'null': 'True', 'through': "orm['archive.Membership']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'years_active': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'})
        },
        'archive.membership': {
            'Meta': {'object_name': 'Membership'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrument': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'now': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Person']"}),
            'years': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'archive.person': {
            'Meta': {'object_name': 'Person'},
            'alive': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'born': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'died': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'})
        },
        'archive.song': {
            'Meta': {'object_name': 'Song'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Artist']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['archive']
