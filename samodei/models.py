# -*- coding: utf-8 -*-
from django.db import models
from util import *
from autoslug import AutoSlugField

from genericm2m.models import BaseGFKRelatedObject, RelatedObjectsDescriptor

class City (models.Model):
	class Meta:
		verbose_name = u'град'
		verbose_name_plural = u'градове'
		
	related = RelatedObjectsDescriptor()
		
	name = models.CharField(max_length=200)
	slug = AutoSlugField(populate_from='name', slugify=unicode_slug)
	
	def __unicode__(self):
		return unicode(self.name)