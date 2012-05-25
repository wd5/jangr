# -*- coding: utf-8 -*-
from autoslug import AutoSlugField
from util import *
from django.db import models
from genericm2m.models import RelatedObjectsDescriptor

from patches.appengine import imagefield
# from jangr.models import City

AlbumSide_Choices = (
	('A', u'Страна А'),
	('B', u'Страна Б'),
)

class TopArticle (models.Model):
	article = models.ForeignKey('Article')


class Article (models.Model):
	u'''Базов клас, от който наследяват всички останали в архива.'''
	title = models.CharField(max_length=64)
	slug = AutoSlugField(populate_from='title',slugify=unicode_slug,unique_with='category')
	category = models.CharField(max_length=64)

	def __unicode__(self):
		return unicode(self.title)


class Person (Article):
	u'''Информация за лице - музикант, текстописец и т.н.'''
	class Meta:
		verbose_name = u'лице'
		verbose_name_plural = u'лица'
	
	alive = models.NullBooleanField(null=True,blank=True)
	born = models.DateField(null=True,blank=True)
	died = models.DateField(null=True,blank=True)
	
	info = models.TextField(blank=True)
	picture = models.ImageField(upload_to='___uploads',blank=True,null=True)
	#picture = imagefield.ImageField(upload_to='archive/artists')
	#picture = models.FileField(upload_to='archive/person',blank=True,null=True)
	
	def save(self):
		if self.alive == None:
			if self.died:
				self.alive = False
			else:
				self.alive = False
			
		super(Person, self).save();
	
	def __unicode__(self):
		return unicode(self.name)
	
		
class Artist (Article):
	u'''Информация за изпълнител или група'''
	class Meta:
		verbose_name = u'група'
		verbose_name_plural = u'групи'

	years_active = models.CharField(max_length=48,blank=True)
	# city = models.CharField(max_length=20,default='София')
	
	description = models.TextField(blank=True)
	#picture = imagefield.ImageField(upload_to='archive/artists',null=True,blank=True)
	#picture = imagefield.ImageField(upload_to='archive/artist',blank=True,null=True)
	picture = models.ImageField(upload_to='___uploads',blank=True,null=True)
	members = models.ManyToManyField(Person,through='Membership',null=True)
	
	def __unicode__(self):
		return unicode(self.name)

		
class Membership (models.Model):
	u'''Информация за членство в група'''
	class Meta:
		verbose_name = u'членство'
		verbose_name_plural = u'членства'

	person = models.ForeignKey(Person)
	group = models.ForeignKey(Artist)
	instrument = models.CharField(max_length=100,blank=True)

	years = models.CharField(max_length=100,blank=True)
	now = models.NullBooleanField()
	
	def __unicode__(self):
		return unicode(self.group.name)
		
		
class Song (Article):
	u'''Информация за музикална композиция (песен)'''
	class Meta:
		verbose_name = u'парче'
		verbose_name_plural = u'парчета'

	original_artists = models.ManyToManyField('Artist')
	
	def __unicode__(self):
		return unicode(self.title)

		
class Album (Article):
	u'''Музикален албум'''
	
	class Meta:
		verbose_name = u'албум'
		verbose_name_plural = u'албуми'
	
	artists = models.ManyToManyField(Artist)
	tracks = models.ManyToManyField(Song,through='AlbumTrack',blank=True)
	
	released = models.DateField(null=True,blank=True)
	publisher = models.CharField(max_length=20,blank=True)
	
	def __unicode__(self):
		return unicode(self.title)
	

class AlbumTrack (models.Model):
	u'''Информация за песен, съдържаща се в албум'''
	class Meta:
		verbose_name = u'трак'
		verbose_name_plural = u'траци'

	song = models.ForeignKey(Song)
	album = models.ForeignKey(Album)
	number = models.PositiveSmallIntegerField(blank=True,null=True)
	side = models.CharField(max_length=1,choices=AlbumSide_Choices,blank=True)
	
	def __unicode__(self):
		#return unicode(str(self.side) + str(self.number) + ". " + self.song.title)
		return unicode(self.song.title)