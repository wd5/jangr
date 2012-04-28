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
	list_display = ('name', 'born', 'died')
	search_fields = ['name']
	form = PersonAdminForm
	
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