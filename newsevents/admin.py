from util import admin
from newsevents.models import Article, Event
from aggregator.models import FeedPost
from documents.models import Document
from django import forms
from django.http import HttpResponse
		
	  
class ArticleAdmin(admin.ModelAdmin):
	readonly_fields = ('views',)
		
	def add_view(self, request, form_url='', extra_context=None):

		feed_post_id = request.GET.get('from_feed_post',None)

		if feed_post_id != None:

			feed_post = FeedPost.objects.get(id=feed_post_id)

			g = request.GET.copy()
			g.update({
				'title':feed_post.title,
				'contents':feed_post.description + u"... \n\n[" + feed_post.url + "](" + feed_post.url + ")",
			})

			request.GET = g

		return super(ArticleAdmin, self).add_view(request, form_url, extra_context)
	
	
class EventAdmin(admin.ModelAdmin):
	list_display = ['title','location','start', 'end']
	
	
admin.site.register(Article, ArticleAdmin)
admin.site.register(Event, EventAdmin)