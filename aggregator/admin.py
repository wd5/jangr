# -*- coding: utf-8 -*-
from django import forms
from util import admin
from aggregator.models import Feed, FeedPost



class FeedAdmin(admin.ModelAdmin):
	pass


	
def make_published(modeladmin, request, queryset):
	queryset.update(reviewed=False)
make_published.short_description = u"Отхвърли избраните постове"

def make_published(modeladmin, request, queryset):
	queryset.update(reviewed=None)
make_published.short_description = u"Направи избраните постове необработени"




	
class FeedPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'from_feed', 'admin_publish_button', 'admin_event_button', 'relevance']
	list_filter = ['reviewed',]
	ordering = ['title',]
	actions = [make_published]
	
	def admin_publish_button(self,post):
		if post.reviewed == True:
			return unicode() + u'<a href="/admin/newsevents/article/add/">Публикуван</a>'
		elif post.reviewed == False:
			return unicode() + u'Отхв&nbsp;-&nbsp;<a href="/admin/newsevents/article/add/?from_feed_post='+unicode(post.id)+u'">Публ</a>&nbsp;|&nbsp;<a href="/admin/newsevents/article/add/">Отм</a>'
		elif post.reviewed == None:
			return unicode() + u'Необр&nbsp;-&nbsp;<a href="/admin/newsevents/article/add/?from_feed_post='+unicode(post.id)+u'">Публ</a>&nbsp;|&nbsp;<a href="/admin/newsevents/article/add/">Отхв</a>'
	admin_publish_button.allow_tags = True
	admin_publish_button.short_description = "Статус"
	
	def admin_event_button(self,post):
		if post.event == None:
			return u'<a href="/admin/newsevents/event/add/">Създай</a>'
		else:
			return u'Има - <a href="/admin/newsevents/event/add/">виж</a>'
	admin_event_button.allow_tags = True
	admin_event_button.short_description = "Събитие"

	
admin.site.register(Feed, FeedAdmin)
admin.site.register(FeedPost, FeedPostAdmin)