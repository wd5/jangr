from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response
from django.template import RequestContext

from archive.models import Artist, Song, Person, Album
import re

from filetransfers.api import prepare_upload

def index(request):
	artist_list = Artist.objects.all()[:7]#Artist.objects.exclude(picture__exact=None).exclude(picture__exact="")[:7]
	all_artists = Artist.objects.count()
	people_list = Person.objects.exclude(picture__exact=None)[:3]
	all_people = Person.objects.count()
	
	return render_to_response(
		'archive/archive-index.html',
		{
			'nav_category':'archive',
		
			'artist_list':artist_list,
			'all_artists':all_artists,
			'person_list':people_list,
			'all_people':all_people
		},
		context_instance=RequestContext(request)
	)

	
#	ARTIST
	
	
def artist_list(request):
	all_artists = Artist.objects.all()
	
	for artist in all_artists:
		artist.hasinfo = False
		if (
			len(artist.description) > 0 or
			#len(artist.song_set.all()) > 0 or
			len(artist.album_set.all()) > 0
		):
			artist.hasinfo = True
			continue
	
	return render_to_response(
		'archive/artist-list.html',
		{
			'nav_category':'archive',
			'artist_list':all_artists
		},
		context_instance=RequestContext(request)
	)

	
def view_artist(request,artist):
	artist_details = Artist.objects.filter(slug=artist)[0]
	p = re.compile('''\[(.*?)\]''',flags=re.M)
	artist_details.description = p.sub('<a href="\g<1>">\g<1></a>',artist_details.description)
	# p = re.compile('''^''',flags=re.M)
	# artist_details.description = p.sub('<p>',artist_details.description)
	# p = re.compile('''$''',flags=re.M)
	# artist_details.description = p.sub('</p>',artist_details.description)
	
	return render_to_response(
		'archive/artist-view.html',
		{
			'nav_category':'archive',
			'artist':artist_details
		},
		context_instance=RequestContext(request)
)

#	SONG
	
	
def view_song(request,artist,song):
	song_info = Song.objects.filter(slug=song)[0]
	artist_info = Artist.objects.filter(slug=artist)[0]
	return render_to_response(
		'archive/song-view.html',
		{
			'nav_category':'archive',
			
			'song':song_info,
			'artist':artist_info,
		},
		context_instance=RequestContext(request)
	)
	

#	ALBUM

def view_album(request,artist,album):
	album_info = Album.objects.filter(slug=album)[0]
	artist_info = Artist.objects.filter(slug=artist)[0]
	return render_to_response(
		'archive/album-view.html',
		{
			'nav_category':'archive',
			
			'album':album_info,
			'artist':artist_info,
		},
		context_instance=RequestContext(request)
	)