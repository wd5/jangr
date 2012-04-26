# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import F

from newsevents.models import Article, Event
from aggregator.models import FeedPost

import datetime
import re


def news_index(request,page=1):
	page = int(page)
	news_list = Article.objects.order_by('-date_added')[(page-1)*10:page*10-1]
	feed_posts_list = FeedPost.objects.filter(reviewed=True)[(page-1)*10:page*10-1]
	
	now = datetime.datetime.now();
	
	for a in news_list:
		a.day = a.date_added.strftime("%d")
		a.month = a.date_added.strftime("%B")
		a.nmonth = a.date_added.month
		a.year = a.date_added.strftime("%Y")
		a.hour = a.date_added.strftime("%H")
		a.minute = a.date_added.strftime("%M")
		
		for i in a.related.all():
			t = type(i.object).__name__
			if t == 'Document' and i.object.type == u'img':
				try:
					a.pic
				except AttributeError:
					a.pic = i.object
	
	return render_to_response(
		'newsevents/news-index.html',
		{
			'nav_category':'news',
		
			'news_list':news_list,
			'feed_posts':feed_posts_list,
		},
		context_instance=RequestContext(request)
	)
	
	
def view_news_item(request,year,month,day,slug):
	article = Article.objects.filter(slug=slug)[0]
	pic = None
	related_documents = []
	related_articles = []
	related_events = []
	
	for i in article.related.all():
		t = type(i.object).__name__
		if t == 'Document':
			related_documents.append(i)
			if i.object.type == u'img' and pic == None:
				pic = i.object
		elif t == 'Article':
			related_articles.append(i)
		elif t == 'Event':
			related_events.append(i)
			
	#article.views = F('views') + 1
	article.save()
			
	return render_to_response(
		'newsevents/news-view.html',
		{
			'nav_category':'news',
			'pic':pic,
			'article':article,
			'documents':related_documents
		},
		context_instance=RequestContext(request)
	)

	
#	EVENTS


def events_index(request,page=1):

	now = datetime.datetime.now()
	today = datetime.datetime.today()

	events = Event.objects.filter(start__gte=today)
	events_now = Event.objects.filter(start__lte=now,end__gte=now)

	calendar = { 'day':now.day, 'month':now.month, 'year':now.year, 'start_weekday':datetime.date(now.year,now.month,1).weekday() }
	
	return render_to_response(
		'newsevents/events-index.html',
		{
			'nav_category':'events',
			'events_now':events_now,
			'events':events,
			'calendar':calendar
		},
		context_instance=RequestContext(request)
	)


def view_event(request,id,slug):

	event = Event.objects.filter(id=id,slug=slug)[0]
	
	
	return render_to_response(
		'newsevents/event-view.html',
		{
			'nav_category':'events',
			'event':event,
		},
		context_instance=RequestContext(request)
	)