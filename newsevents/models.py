# -*- coding: utf-8 -*-
from autoslug import AutoSlugField
#from util import *

from django.db import models
import util
#from django.db.models import Model, permalink
from documents.models import Document
from catalog.models import CatalogEntry
from django.contrib.auth.models import User
from djangotoolbox import fields

from genericm2m.models import RelatedObjectsDescriptor


class Article (models.Model):
	u'''Новина, статия или друго писание'''
	class Meta:
		verbose_name = u'статия'
		verbose_name_plural = u'статии'
		
	related = RelatedObjectsDescriptor()
	
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200,blank=True)
	slug = AutoSlugField(populate_from='title', slugify=util.unicode_slug)
	
	date_added = models.DateTimeField(auto_now=False,auto_now_add=True)
	date_changed = models.DateTimeField(auto_now=True,auto_now_add=False)
	views = models.PositiveIntegerField(default=0)
	
	contents = models.TextField(blank=True)
	
	def __unicode__(self):
		return unicode(self.title)
		
	@models.permalink
	def get_absolute_url(self):
		return (
			'newsevents.views.view_news_item',
			(),
			{
				'year': self.date_added.year,
				'month': self.date_added.strftime('%m'),
				'day': self.date_added.strftime('%d'),
				'slug': self.slug
			}
		)

class EventAttendee(models.Model):
	user = models.ForeignKey(User)
	event = models.ForeignKey('Event')
	certainty = models.BooleanField(default=False)
		
class Event (models.Model):
	u'''Концерт или друго събитие'''
	class Meta:
		verbose_name = u'събитие'
		verbose_name_plural = u'събития'
		
	related = RelatedObjectsDescriptor()
	
	title = models.CharField(max_length=200)
	slug = AutoSlugField(populate_from='title', slugify=util.unicode_slug)
	
	date_added = models.DateTimeField(auto_now=False,auto_now_add=True)
	date_changed = models.DateTimeField(auto_now=True,auto_now_add=False)
	
	start = models.DateTimeField(blank=True,null=True)
	end = models.DateTimeField(blank=True,null=True)
	description = models.TextField(blank=True)
	
	location = models.ForeignKey(CatalogEntry,blank=True,null=True)

	# attending = fields.ListField(editable=False)
	# attending_maybe = fields.ListField(editable=False)
	
	def __unicode__(self):
		return unicode(self.title)

	@models.permalink
	def get_absolute_url(self):
		return (
			'newsevents.views.view_event',
			(),
			{
				'id': self.id,
				'slug': self.slug
			}
		)