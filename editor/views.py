from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import F

from aggregator.models import Feed, FeedPost

def index(request):
	if 'do' in request.GET:
		if request.GET['do'] =='feed-vote':
			feed_post = FeedPost.objects.filter(id=request.GET['id'])
			
			for i in feed_post:
				if request.GET['vote'] == 'plus':
					i.relevance = F('relevance') + 1
				elif request.GET['vote'] == 'minus':
					i.relevance = F('relevance') - 1
					
				i.save()

	if request.is_ajax():
		return HttpResponse()
		
	else:
		if 'feed_posts' in request.GET:
			how_many_feed_posts = 3
		else:
			how_many_feed_posts = 1
			
		feed_posts = FeedPost.objects.exclude(published=True).order_by('?')

		return render_to_response(
			'editor/index.html',
			{
				'feed_posts': feed_posts[:how_many_feed_posts],
			},
			context_instance=RequestContext(request)
		)