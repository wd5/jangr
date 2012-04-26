from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import django.contrib.auth.views
from util import rescale
import csv

from archive.models import Artist, Song, Person
from newsevents.models import Article, Event
	
def homepage(request):
	if request.user.is_authenticated():
		artist_list = Artist.objects.exclude(picture=None)[:4]
		news_list = Article.objects.all()[:2]
		
		return render_to_response(
			'homepage/index.html',
			{
				'artist_list':artist_list,
				'news_list':news_list
			},
			context_instance=RequestContext(request)
		)
		
	else:
		return render_to_response('prelaunch/prelaunch.html',{},context_instance=RequestContext(request))
	
def view_image(request, path='none', width=-1, height=-1):
	return rescale(path, width, height, force=True)