# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response
from django.template import RequestContext

from archive.models import Artist
from catalog.models import CatalogEntry

import re

def index(request):

	venues = CatalogEntry.objects.filter(type="ven")
	studios = CatalogEntry.objects.filter(type="stu")
	services = CatalogEntry.objects.filter(type="svc")
	shops = CatalogEntry.objects.filter(type="shp")
	
	return render_to_response(
		'catalog/catalog-index.html',
		{
			'categories': [
				(u'Сцени',venues),
				(u'Студиа',studios),
				(u'Услуги',services),
				(u'Магазини',shops),
			],
			'nav_category':'catalog',
		},
		context_instance=RequestContext(request)
	)
	
	
def view_item(request,item_slug):

	item = CatalogEntry.objects.filter(slug=item_slug)[0]
	bands = Artist.objects.all()[0:30]
	
	return render_to_response(
		'catalog/catalog-item.html',
		{
			'item':item,
			'bands':bands,
			'nav_category':'catalog',
		},
		context_instance=RequestContext(request)
	)