# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Album'
        db.create_table('archive_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('released', self.gf('django.db.models.fields.DateField')()),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=20)),
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
            ('number', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('archive', ['AlbumTrack'])


    def backwards(self, orm):
        
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
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'released': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tracks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['archive.Song']", 'through': "orm['archive.AlbumTrack']", 'symmetrical': 'False'})
        },
        'archive.albumtrack': {
            'Meta': {'object_name': 'AlbumTrack'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Song']"})
        },
        'archive.artist': {
            'Meta': {'object_name': 'Artist'},
            'city': ('django.db.models.fields.CharField', [], {'default': "'\\xd0\\xa1\\xd0\\xbe\\xd1\\x84\\xd0\\xb8\\xd1\\x8f'", 'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['archive.Person']", 'null': 'True', 'through': "orm['archive.Membership']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'picture': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'picture': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'})
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
