# -*- coding: utf-8 -*-
from util import admin
from archive.models import Artist, Song, Person, Album
from django import forms

	
class MembershipInline(admin.TabularInline):
	model = Artist.members.through
	extra = 5
	
class AlbumTrackInline(admin.TabularInline):
	model = Album.tracks.through
	extra = 10

class SongAdmin(admin.ModelAdmin):
	search_fields = ['title']

class PersonAdminForm(forms.ModelForm):
	class Meta:
		model = Person

	def __init__(self, *args, **kwargs):
		super(PersonAdminForm, self).__init__(*args, **kwargs)
		# self.fields['picture']=forms.CharField()

class PersonAdmin(admin.ModelAdmin):
	list_display = ['person_infobox',]
	search_fields = ['name',]
	form = PersonAdminForm

	def person_infobox(self,person):

		if person.born and not person.died:
			dates = u'р. ' + unicode(person.born)
		elif person.born and person.died:
			dates = unicode(person.born) + u"&mdash;" + unicode(person.died)
		else:
			dates = ""

		return \
			u"""<div style="width:36px;height:36px;background:black;float:left;margin-right:5px">&nbsp;</div>""" + \
			unicode(person.name) + (u"" if person.alive else u"&dagger;") + u"<br />" + \
			u'<div style="font-weight:normal;color:#777;box-shadow:0 1px 0 #fff">' + dates + u"</div>"
	person_infobox.allow_tags=True

	
class ArtistAdmin(admin.ModelAdmin):
	list_display = ('name','years_active')
	inlines = [MembershipInline,]
	
class AlbumAdmin(admin.ModelAdmin):
	list_display = ('title','released')
	inlines = [AlbumTrackInline,]
	
	
admin.site.register(Song, SongAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Album, AlbumAdmin)