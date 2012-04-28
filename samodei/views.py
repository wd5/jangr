from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import django.contrib.auth.views
import csv
from filetransfers.api import serve_file
from django.shortcuts import get_object_or_404

from django.db.models import Model
from archive.models import Artist, Song, Person
from newsevents.models import Article, Event
from documents.models import Document

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


def download_handler(request, key, fieldname):
	a = Person.objects.filter(pk=key)[0]
	return serve_file(request, a.picture)