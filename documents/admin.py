from util import admin
from documents.models import *
	
class DocumentInCollectionInline(admin.TabularInline):
	model = DocumentInCollection
	ordering = ('order',)

class DocumentAdmin(admin.ModelAdmin):
	list_display = ('title','type')
	pass
	
class DocumentCollectionAdmin(admin.ModelAdmin):
	list_display = ('title',)
	inlines = [ DocumentInCollectionInline ]
	pass
	
admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentCollection, DocumentCollectionAdmin)