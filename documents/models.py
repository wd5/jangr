# -*- coding: utf-8 -*-
from autoslug import AutoSlugField
# from util import *
from django.db import models
import util

from genericm2m.models import BaseGFKRelatedObject, RelatedObjectsDescriptor

DocumentTypes = (
	('lyr', u'Текст на песен'),
	('crd', u'Текст и акорди на песен'),
	('dsc', u'Информация за песента'),
	('tab', u'Табулатура в текстов вид'),
	('gp5', u'Табулатура в Guitar Pro формат'),
	('txt', u'Текстов документ'),
	('img', u'Изображение'),
	('vid', u'Клип'),
	('aud', u'Звук'),
	('bit', u'Торент'),
	('dru', u'Нещо друго'),
	('nil', u'Нищо')
)


class DocumentInCollection (models.Model):
	document = models.ForeignKey('Document')
	album = models.ForeignKey('DocumentCollection')
	order = models.IntegerField()


class DocumentCollection (models.Model):
	class Meta:
		verbose_name = u'колекция от документи'
		verbose_name_plural = u'колекции от документи'
		
	related = RelatedObjectsDescriptor()
	
	title = models.CharField(max_length=64)
	slug = AutoSlugField(populate_from='title', slugify=util.unicode_slug)
	
	documents = models.ManyToManyField('Document',through='DocumentInAlbum')
	
	def __unicode__(self):
		return unicode(self.title)
		

class Document (models.Model):
	u'''Документ - текст, акорди, медиен файл, линк и т.н.'''
	class Meta:
		verbose_name = u'документ'
		verbose_name_plural = u'документи'

	related = RelatedObjectsDescriptor()
	
	title = models.CharField(max_length=64)
	slug = AutoSlugField(populate_from='title', slugify=util.unicode_slug)
	
	type = models.CharField(max_length=3,choices=DocumentTypes,default='nil')
	date_added = models.DateTimeField(auto_now=False,auto_now_add=True,null=True)
	date_changed = models.DateTimeField(auto_now=True,auto_now_add=False,null=True)
	
	text = models.TextField(blank=True)
	url = models.URLField(blank=True)
	file = models.FileField(upload_to='documents/misc',blank=True,null=True)
	image = models.ImageField(upload_to='documents/misc',null=True,blank=True)
	
	def __unicode__(self):
		return unicode(self.title)
	
	def get_url(self):
		return unicode(self.type + u'/' + self.slug)
		
	get_url = property(get_url)