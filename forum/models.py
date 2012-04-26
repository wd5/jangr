# -*- coding: utf-8 -*-
from autoslug import AutoSlugField
from util import *

class ForumSection (models.Model):
	parent = models.ForeignKey('self',blank=True,null=True)
	name = models.CharField(max_length=100)
	slug = models.CharField(max_length=20,blank=True)
	description = models.CharField(max_length=200,blank=True)
	can_have_threads = models.BooleanField(default=True)
	
	def __unicode__(self):
		return unicode(self.name)

class ForumThread (models.Model):
	parent = models.ForeignKey('ForumSection')
	title = models.CharField(max_length=200)
	
	def __unicode__(self):
		return unicode(self.title)

	
class ForumPost (models.Model):
	parent = models.ForeignKey('ForumThread')
	
#	def __unicode__(self):
#		return unicode(self.name)


"""
class CatalogEntry (models.Model):
	class Meta:
		verbose_name = u'запис'
		verbose_name_plural = u'записи'
		
	title = models.CharField(max_length=200)
	type = models.CharField(max_length=3,choices=PlaceTypes,default='nil')
	slug = AutoSlugField(populate_from='title', slugify=unicode_slug)
	city = models.ForeignKey(City,blank=True,null=True)
	description = models.TextField(blank=True)
	contact_data = models.TextField(blank=True)
	
	def __unicode__(self):
		return unicode(self.title)
	
	
class CatalogReview (models.Model):
	class Meta:
		verbose_name = u'оценка'
		verbose_name_plural = u'оценки'
		
	for_entry = models.ForeignKey('CatalogEntry')
	title = models.CharField(max_length=200)
	text = models.TextField()
	rating = models.PositiveIntegerField(blank=True,null=True)
	helpful = models.PositiveIntegerField(blank=True,null=True)
	unhelpful = models.PositiveIntegerField(blank=True,null=True)


class Classified (models.Model):
	class Meta:
		verbose_name = u'обява'
		verbose_name_plural = u'обяви'

	title = models.CharField(max_length=200)"""