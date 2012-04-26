# -*- coding: utf-8 -*-
from autoslug import AutoSlugField
from util import *
from django.db import models
from newsevents.models import Article, Event

class Feed (models.Model):
	u'''RSS/Atom фийд'''
	class Meta:
		verbose_name = u'фийд'
		verbose_name_plural = u'фийдове'
		
	title = models.CharField(max_length=200)
	slug = AutoSlugField(populate_from='title', slugify=unicode_slug)
	
	feed_url = models.URLField()
	site_url = models.URLField(blank=True)
	
	last_parsed = models.DateTimeField(blank=True,null=True)
	
	moderate = models.BooleanField(default=True)

	def __unicode__(self):
		return unicode(self.title)
	

class FeedPost (models.Model):
	class Meta:
		verbose_name = u'пост от фийд'
		verbose_name_plural = u'постове от фийдове'
		
	from_feed = models.ForeignKey('Feed')
		
	title = models.CharField(max_length=200)
	slug = AutoSlugField(populate_from='title', slugify=unicode_slug)
	url = models.URLField()
	description = models.TextField(blank=True)
	hash = models.CharField(max_length=64,editable=False)
	
	relevance = models.SmallIntegerField(default=0)
	reviewed = models.NullBooleanField(default=False)
	article = models.ForeignKey(Article,null=True,blank=True)
	event = models.ForeignKey(Event,null=True,blank=True)
	
	date_received = models.DateTimeField(blank=True,null=True)
	date_published = models.DateTimeField(blank=True,null=True)
		
	def __unicode__(self):
		return unicode(self.title)