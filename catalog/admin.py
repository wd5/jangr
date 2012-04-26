# -*- coding: utf-8 -*-
from util import admin
from catalog.models import CatalogEntry, CatalogReview

class CatalogEntryAdmin(admin.ModelAdmin):
	list_display = ['title', 'type', 'city',]
	pass
	
class CatalogReviewAdmin(admin.ModelAdmin):
	pass
	

admin.site.register(CatalogEntry, CatalogEntryAdmin)
admin.site.register(CatalogReview, CatalogReviewAdmin)