# -*- coding: utf-8 -*-
from autoslug import AutoSlugField
from samodei.models import City
from util import *
from archive.models import Artist
from documents.models import Document, DocumentCollection
from genericm2m.models import RelatedObjectsDescriptor

PlaceTypes = (
	('ven', u'Сцена (клуб и т.н.)'),
	('stu', u'Студио'),
	('shp', u'Магазин'),
	('svc', u'Услуги (майстор; рентал)'),
	('nil', u'Други')
)

class CatalogEntry (models.Model):
	class Meta:
		verbose_name = u'запис'
		verbose_name_plural = u'записи'
		
	related = RelatedObjectsDescriptor()
		
	title = models.CharField(max_length=200)
	type = models.CharField(max_length=3,choices=PlaceTypes,default='nil')
	slug = AutoSlugField(populate_from='title', slugify=unicode_slug)
	city = models.ForeignKey(City,blank=True,null=True)
	description = models.TextField(blank=True)
	contact_data = models.TextField(blank=True)
	
	related_artists = models.ManyToManyField(Artist,blank=True,null=True)
	
	splash = models.ForeignKey(Document,blank=True,null=True)
	gallery = models.ForeignKey(DocumentCollection,blank=True,null=True)
	
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

	title = models.CharField(max_length=200)