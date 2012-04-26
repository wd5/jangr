from util import admin
from archive.models import Artist, Song, Person, Album

	
class MembershipInline(admin.TabularInline):
	model = Artist.members.through
	extra = 5
	
class AlbumTrackInline(admin.TabularInline):
	model = Album.tracks.through
	extra = 10

class SongAdmin(admin.ModelAdmin):
	search_fields = ['title']
	pass

class PersonAdmin(admin.ModelAdmin):
	list_display = ('name', 'born', 'died')
	search_fields = ['name']
	pass
	
class ArtistAdmin(admin.ModelAdmin):
	list_display = ('name','years_active','city')
	inlines = [MembershipInline,]
	pass
	
class AlbumAdmin(admin.ModelAdmin):
	list_display = ('title','released')
	inlines = [AlbumTrackInline,]
	pass
	
	
admin.site.register(Song, SongAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Album, AlbumAdmin)